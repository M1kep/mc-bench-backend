"""add run stage modeling

Revision ID: 665d4b9d70a6
Revises: 848301f47914
Create Date: 2024-12-09 00:56:04.760065

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "665d4b9d70a6"
down_revision: Union[str, None] = "848301f47914"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

RUN_STAGE_STATES = [
    "PENDING",
    "IN_PROGRESS",
    "COMPLETED",
    "FAILED",
    "IN_RETRY",
]

RUN_STATES = [
    "CREATED",
    "IN_PROGRESS",
    "COMPLETED",
    "FAILED",
    "IN_RETRY",
]

GENERATION_STATES = [
    "CREATED",
    "IN_PROGRESS",
    "COMPLETED",
    "PARTIAL_FAILED",
    "IN_RETRY",
    "FAILED",
]

STAGES = [
    "PROMPT_EXECUTION",
    "RESPONSE_PARSING",
    "BUILDING",
    "EXPORTING_CONTENT",
    "POST_PROCESSING",
    "PREPARING_SAMPLE",
]


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "run_stage_state",
        sa.Column("id", sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column(
            "created", sa.TIMESTAMP(), server_default=sa.text("now()"), nullable=False
        ),
        sa.Column("created_by", sa.Integer(), nullable=False),
        sa.Column("last_modified", sa.TIMESTAMP(), nullable=True),
        sa.Column("last_modified_by", sa.Integer(), nullable=True),
        sa.Column(
            "external_id",
            sa.UUID(),
            server_default=sa.text("uuid_generate_v4()"),
            nullable=False,
        ),
        sa.Column("slug", sa.String(), nullable=False),
        sa.ForeignKeyConstraint(
            ["created_by"],
            ["auth.user.id"],
        ),
        sa.ForeignKeyConstraint(
            ["last_modified_by"],
            ["auth.user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("slug"),
        schema="specification",
    )
    op.create_table(
        "stage",
        sa.Column("id", sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column(
            "created", sa.TIMESTAMP(), server_default=sa.text("now()"), nullable=False
        ),
        sa.Column("created_by", sa.Integer(), nullable=False),
        sa.Column("last_modified", sa.TIMESTAMP(), nullable=True),
        sa.Column("last_modified_by", sa.Integer(), nullable=True),
        sa.Column(
            "external_id",
            sa.UUID(),
            server_default=sa.text("uuid_generate_v4()"),
            nullable=False,
        ),
        sa.Column("slug", sa.String(), nullable=False),
        sa.ForeignKeyConstraint(
            ["created_by"],
            ["auth.user.id"],
        ),
        sa.ForeignKeyConstraint(
            ["last_modified_by"],
            ["auth.user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("slug"),
        schema="specification",
    )
    op.create_table(
        "run_stage",
        sa.Column("id", sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column(
            "created", sa.TIMESTAMP(), server_default=sa.text("now()"), nullable=True
        ),
        sa.Column(
            "external_id",
            sa.UUID(),
            server_default=sa.text("uuid_generate_v4()"),
            nullable=False,
        ),
        sa.Column("run_id", sa.Integer(), nullable=False),
        sa.Column("stage_id", sa.Integer(), nullable=False),
        sa.Column("state_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["run_id"],
            ["specification.run.id"],
        ),
        sa.ForeignKeyConstraint(
            ["stage_id"],
            ["specification.stage.id"],
        ),
        sa.ForeignKeyConstraint(
            ["state_id"],
            ["specification.run_stage_state.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        schema="specification",
    )

    for state in RUN_STATES:
        op.execute(
            sa.text(
                """\
                INSERT INTO specification.run_state (created_by, slug) values (
                    (SELECT id from auth.user where username = 'SYSTEM'),
                    :slug
                )
                ON CONFLICT (slug) DO NOTHING
            """
            ).bindparams(slug=state)
        )

    for state in GENERATION_STATES:
        op.execute(
            sa.text(
                """\
                INSERT INTO specification.generation_state (created_by, slug) values (
                    (SELECT id from auth.user where username = 'SYSTEM'),
                    :slug
                )
                ON CONFLICT (slug) DO NOTHING
            """
            ).bindparams(slug=state)
        )

    for state in RUN_STAGE_STATES:
        op.execute(
            sa.text(
                """\
                INSERT INTO specification.run_stage_state (created_by, slug) values (
                    (SELECT id from auth.user where username = 'SYSTEM'),
                    :slug
                )
                ON CONFLICT (slug) DO NOTHING
            """
            ).bindparams(slug=state)
        )

    for stage in STAGES:
        op.execute(
            sa.text(
                """\
                INSERT INTO specification.stage (created_by, slug) values (
                    (SELECT id from auth.user where username = 'SYSTEM'),
                    :slug
                )
                ON CONFLICT (slug) DO NOTHING
            """
            ).bindparams(slug=stage)
        )

    # ### end Alembic commands ###


def downgrade() -> None:
    raise RuntimeError("Upgrades only")
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("run_stage", schema="specification")
    op.drop_table("stage", schema="specification")
    op.drop_table("run_stage_state", schema="specification")
    # ### end Alembic commands ###

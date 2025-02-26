"""Add prompt, model, and template join tables

Revision ID: 00f736acf066
Revises: 8fff682fdaa3
Create Date: 2025-02-25 12:37:55.301824

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "00f736acf066"
down_revision: Union[str, None] = "8fff682fdaa3"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "model_experimental_state_proposal",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column(
            "external_id",
            sa.UUID(),
            server_default=sa.text("uuid_generate_v4()"),
            nullable=False,
        ),
        sa.Column(
            "created", sa.TIMESTAMP(), server_default=sa.text("now()"), nullable=False
        ),
        sa.Column("created_by", sa.Integer(), nullable=False),
        sa.Column("model_id", sa.Integer(), nullable=False),
        sa.Column("new_experiment_state_id", sa.Integer(), nullable=False),
        sa.Column("log_id", sa.Integer(), nullable=True),
        sa.Column("accepted", sa.Boolean(), nullable=True),
        sa.Column("accepted_at", sa.TIMESTAMP(), nullable=True),
        sa.Column("accepted_by", sa.Integer(), nullable=True),
        sa.Column("accepted_log_id", sa.Integer(), nullable=True),
        sa.Column("rejected", sa.Boolean(), nullable=True),
        sa.Column("rejected_at", sa.TIMESTAMP(), nullable=True),
        sa.Column("rejected_by", sa.Integer(), nullable=True),
        sa.Column("rejected_log_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["accepted_by"],
            ["auth.user.id"],
        ),
        sa.ForeignKeyConstraint(
            ["accepted_log_id"],
            ["research.log.id"],
        ),
        sa.ForeignKeyConstraint(
            ["created_by"],
            ["auth.user.id"],
        ),
        sa.ForeignKeyConstraint(
            ["log_id"],
            ["research.log.id"],
        ),
        sa.ForeignKeyConstraint(
            ["model_id"],
            ["specification.model.id"],
        ),
        sa.ForeignKeyConstraint(
            ["new_experiment_state_id"],
            ["research.experimental_state.id"],
        ),
        sa.ForeignKeyConstraint(
            ["rejected_by"],
            ["auth.user.id"],
        ),
        sa.ForeignKeyConstraint(
            ["rejected_log_id"],
            ["research.log.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        schema="research",
    )
    op.create_table(
        "prompt_experimental_state_proposal",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column(
            "external_id",
            sa.UUID(),
            server_default=sa.text("uuid_generate_v4()"),
            nullable=False,
        ),
        sa.Column(
            "created", sa.TIMESTAMP(), server_default=sa.text("now()"), nullable=False
        ),
        sa.Column("created_by", sa.Integer(), nullable=False),
        sa.Column("prompt_id", sa.Integer(), nullable=False),
        sa.Column("new_experiment_state_id", sa.Integer(), nullable=False),
        sa.Column("log_id", sa.Integer(), nullable=True),
        sa.Column("accepted", sa.Boolean(), nullable=True),
        sa.Column("accepted_at", sa.TIMESTAMP(), nullable=True),
        sa.Column("accepted_by", sa.Integer(), nullable=True),
        sa.Column("accepted_log_id", sa.Integer(), nullable=True),
        sa.Column("rejected", sa.Boolean(), nullable=True),
        sa.Column("rejected_at", sa.TIMESTAMP(), nullable=True),
        sa.Column("rejected_by", sa.Integer(), nullable=True),
        sa.Column("rejected_log_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["accepted_by"],
            ["auth.user.id"],
        ),
        sa.ForeignKeyConstraint(
            ["accepted_log_id"],
            ["research.log.id"],
        ),
        sa.ForeignKeyConstraint(
            ["created_by"],
            ["auth.user.id"],
        ),
        sa.ForeignKeyConstraint(
            ["log_id"],
            ["research.log.id"],
        ),
        sa.ForeignKeyConstraint(
            ["new_experiment_state_id"],
            ["research.experimental_state.id"],
        ),
        sa.ForeignKeyConstraint(
            ["prompt_id"],
            ["specification.prompt.id"],
        ),
        sa.ForeignKeyConstraint(
            ["rejected_by"],
            ["auth.user.id"],
        ),
        sa.ForeignKeyConstraint(
            ["rejected_log_id"],
            ["research.log.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        schema="research",
    )
    op.create_table(
        "template_experimental_state_proposal",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column(
            "external_id",
            sa.UUID(),
            server_default=sa.text("uuid_generate_v4()"),
            nullable=False,
        ),
        sa.Column(
            "created", sa.TIMESTAMP(), server_default=sa.text("now()"), nullable=False
        ),
        sa.Column("created_by", sa.Integer(), nullable=False),
        sa.Column("template_id", sa.Integer(), nullable=False),
        sa.Column("new_experiment_state_id", sa.Integer(), nullable=False),
        sa.Column("log_id", sa.Integer(), nullable=True),
        sa.Column("accepted", sa.Boolean(), nullable=True),
        sa.Column("accepted_at", sa.TIMESTAMP(), nullable=True),
        sa.Column("accepted_by", sa.Integer(), nullable=True),
        sa.Column("accepted_log_id", sa.Integer(), nullable=True),
        sa.Column("rejected", sa.Boolean(), nullable=True),
        sa.Column("rejected_at", sa.TIMESTAMP(), nullable=True),
        sa.Column("rejected_by", sa.Integer(), nullable=True),
        sa.Column("rejected_log_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["accepted_by"],
            ["auth.user.id"],
        ),
        sa.ForeignKeyConstraint(
            ["accepted_log_id"],
            ["research.log.id"],
        ),
        sa.ForeignKeyConstraint(
            ["created_by"],
            ["auth.user.id"],
        ),
        sa.ForeignKeyConstraint(
            ["log_id"],
            ["research.log.id"],
        ),
        sa.ForeignKeyConstraint(
            ["new_experiment_state_id"],
            ["research.experimental_state.id"],
        ),
        sa.ForeignKeyConstraint(
            ["rejected_by"],
            ["auth.user.id"],
        ),
        sa.ForeignKeyConstraint(
            ["rejected_log_id"],
            ["research.log.id"],
        ),
        sa.ForeignKeyConstraint(
            ["template_id"],
            ["specification.template.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        schema="research",
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    raise RuntimeError("Upgrades only")
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("template_experimental_state_proposal", schema="research")
    op.drop_table("prompt_experimental_state_proposal", schema="research")
    op.drop_table("model_experimental_state_proposal", schema="research")
    # ### end Alembic commands ###

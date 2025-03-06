"""add_leaderboard_tables

Revision ID: 47fc21ce40a3
Revises: 9b7eed150ea2
Create Date: 2025-03-06 00:13:44.133290

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "47fc21ce40a3"
down_revision: Union[str, None] = "9b7eed150ea2"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "model_leaderboard",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column(
            "created", sa.TIMESTAMP(), server_default=sa.text("now()"), nullable=False
        ),
        sa.Column(
            "last_updated",
            sa.TIMESTAMP(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column("model_id", sa.Integer(), nullable=False),
        sa.Column("metric_id", sa.Integer(), nullable=False),
        sa.Column("test_set_id", sa.Integer(), nullable=False),
        sa.Column("tag_id", sa.Integer(), nullable=True),
        sa.Column("elo_score", sa.Float(), nullable=False),
        sa.Column("vote_count", sa.Integer(), nullable=False),
        sa.Column("win_count", sa.Integer(), nullable=False),
        sa.Column("loss_count", sa.Integer(), nullable=False),
        sa.Column("tie_count", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["metric_id"],
            ["scoring.metric.id"],
        ),
        sa.ForeignKeyConstraint(
            ["model_id"],
            ["specification.model.id"],
        ),
        sa.ForeignKeyConstraint(
            ["tag_id"],
            ["specification.tag.id"],
        ),
        sa.ForeignKeyConstraint(
            ["test_set_id"],
            ["sample.test_set.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint(
            "model_id",
            "metric_id",
            "test_set_id",
            "tag_id",
            name="unique_model_leaderboard_entry",
        ),
        schema="scoring",
    )
    op.create_table(
        "sample_leaderboard",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column(
            "created", sa.TIMESTAMP(), server_default=sa.text("now()"), nullable=False
        ),
        sa.Column(
            "last_updated",
            sa.TIMESTAMP(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column("sample_id", sa.Integer(), nullable=False),
        sa.Column("metric_id", sa.Integer(), nullable=False),
        sa.Column("test_set_id", sa.Integer(), nullable=False),
        sa.Column("elo_score", sa.Float(), nullable=False),
        sa.Column("vote_count", sa.Integer(), nullable=False),
        sa.Column("win_count", sa.Integer(), nullable=False),
        sa.Column("loss_count", sa.Integer(), nullable=False),
        sa.Column("tie_count", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["metric_id"],
            ["scoring.metric.id"],
        ),
        sa.ForeignKeyConstraint(
            ["sample_id"],
            ["sample.sample.id"],
        ),
        sa.ForeignKeyConstraint(
            ["test_set_id"],
            ["sample.test_set.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint(
            "sample_id",
            "metric_id",
            "test_set_id",
            name="unique_sample_leaderboard_entry",
        ),
        schema="scoring",
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    raise RuntimeError("Upgrades only")
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("sample_leaderboard", schema="scoring")
    op.drop_table("model_leaderboard", schema="scoring")
    # ### end Alembic commands ###

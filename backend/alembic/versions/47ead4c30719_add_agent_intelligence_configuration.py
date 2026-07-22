"""Add agent intelligence configuration

Revision ID: 47ead4c30719
Revises: 796871a99d87
Create Date: 2026-07-22 01:25:41.715155

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '47ead4c30719'
down_revision: Union[str, Sequence[str], None] = '796871a99d87'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Add new agent intelligence configuration columns
    op.add_column(
        "agents",
        sa.Column("backstory", sa.String(length=1000), nullable=True),
    )

    op.add_column(
        "agents",
        sa.Column("temperature", sa.Float(), nullable=True),
    )

    op.add_column(
        "agents",
        sa.Column("max_tokens", sa.Integer(), nullable=True),
    )

    op.add_column(
        "agents",
        sa.Column("is_active", sa.Boolean(), nullable=True),
    )


def downgrade() -> None:
    """Downgrade schema."""
    # Remove the four columns added in upgrade
    op.drop_column("agents", "is_active")
    op.drop_column("agents", "max_tokens")
    op.drop_column("agents", "temperature")
    op.drop_column("agents", "backstory") 
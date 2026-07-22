"""Add execution order to agents

Revision ID: af7994b2a9b0
Revises: 47ead4c30719
Create Date: 2026-07-22 03:52:16.720010

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'af7994b2a9b0'
down_revision: Union[str, Sequence[str], None] = '47ead4c30719'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    # Step 1: Add the new column as nullable
    op.add_column(
        "agents",
        sa.Column(
            "execution_order",
            sa.Integer(),
            nullable=True,
        ),
    )

    # Step 2: Populate existing rows
    op.execute(
        "UPDATE agents SET execution_order = 1 WHERE execution_order IS NULL"
    )

    # Step 3: Make the column required
    op.alter_column(
        "agents",
        "execution_order",
        nullable=False,
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_column("agents", "execution_order")
"""add lat lon to locations

Revision ID: 6f0828c0d507
Revises: 4321155c439a
Create Date: 2026-02-04 17:48:44.320032

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6f0828c0d507'
down_revision: Union[str, Sequence[str], None] = '4321155c439a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('locations', sa.Column('latitude', sa.Float(), nullable=True))
    op.add_column('locations', sa.Column('longitude', sa.Float(), nullable=True))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('locations', 'latitude')
    op.drop_column('locations', 'longitude')

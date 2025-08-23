"""add icon url column

Revision ID: 23a1b6dce235
Revises: 221d4f48146a
Create Date: 2025-08-09 08:36:40.666572

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '23a1b6dce235'
down_revision: Union[str, None] = '221d4f48146a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users',
      sa.Column('icon_url', sa.String(length=256), nullable=True, unique=True, default=None)
    )


def downgrade() -> None:
    op.drop_column('users', 'icon_url')

"""empty message

Revision ID: 96a0304b8280
Revises: 4725970059da, b8a2586a05a4
Create Date: 2024-08-09 17:49:49.486809

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '96a0304b8280'
down_revision: Union[str, None] = ('4725970059da', 'b8a2586a05a4')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

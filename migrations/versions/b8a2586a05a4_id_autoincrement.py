"""id autoincrement

Revision ID: b8a2586a05a4
Revises: 8b7557fca0d6
Create Date: 2024-08-09 16:49:11.256861

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = 'b8a2586a05a4'
down_revision = '8b7557fca0d6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    """Apply the migration: Alter the 'id' column to be an autoincrementing primary key."""
    with op.batch_alter_table('users') as batch_op:
        batch_op.alter_column('id', existing_type=sa.Integer, autoincrement=True, nullable=False)

def downgrade() -> None:
    """Revert the migration: Remove the autoincrement from the 'id' column."""
    with op.batch_alter_table('users') as batch_op:
        batch_op.alter_column('id', existing_type=sa.Integer, autoincrement=False, nullable=False)
"""create cpf two

Revision ID: 8b7557fca0d6
Revises: eea3ed3fd2fb
Create Date: 2024-08-09 16:41:18.485831

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = '8b7557fca0d6'
down_revision = 'eea3ed3fd2fb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    """Apply the migration: Add 'id' column and create a unique constraint on 'cpf'."""
    with op.batch_alter_table('users') as batch_op:
        batch_op.add_column(sa.Column('id', sa.Integer(), nullable=False))
        batch_op.create_unique_constraint('uq_users_cpf', 'cpf')

def downgrade() -> None:
    """Revert the migration: Drop the unique constraint on 'cpf' and remove 'id' column."""
    with op.batch_alter_table('users') as batch_op:
        batch_op.drop_constraint('uq_users_cpf', type_='unique')
        batch_op.drop_column('id')

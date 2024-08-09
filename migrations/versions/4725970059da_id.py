"""id

Revision ID: 4725970059da
Revises: b8a2586a05a4
Create Date: 2024-08-09 16:55:45.488530

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = '4725970059da'
down_revision = '8b7557fca0d6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    """Apply the migration: Make 'cpf' the primary key and ensure 'id' is auto-incrementing."""
    with op.batch_alter_table('users') as batch_op:
        batch_op.alter_column('id', existing_type=sa.Integer(), autoincrement=True, nullable=False)
        batch_op.create_primary_key('pk_users_cpf', ['cpf'])  # Make 'cpf' the primary key

def downgrade() -> None:
    """Revert the migration: Drop the primary key on 'cpf' and restore the previous state."""
    with op.batch_alter_table('users') as batch_op:
        batch_op.drop_constraint('pk_users_cpf', type_='primary')
        batch_op.alter_column('id', existing_type=sa.Integer(), autoincrement=False, nullable=False)

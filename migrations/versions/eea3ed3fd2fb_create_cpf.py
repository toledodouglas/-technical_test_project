"""create cpf

Revision ID: eea3ed3fd2fb
Revises: 74f39286e2f6
Create Date: 2024-08-09 16:33:27.829092

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'eea3ed3fd2fb'
down_revision: Union[str, None] = '74f39286e2f6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    with op.batch_alter_table('users') as batch_op:
        # Drop the existing primary key (if any)
        batch_op.drop_column('id')
        
        # Make cpf the primary key
        batch_op.create_primary_key('pk_users', ['cpf'])


def downgrade():
    with op.batch_alter_table('users') as batch_op:
        # Recreate the id column
        batch_op.add_column(sa.Column('id', sa.Integer, primary_key=True, autoincrement=True))
        
        # Drop the cpf primary key constraint
        batch_op.drop_constraint('pk_users', type_='primary')
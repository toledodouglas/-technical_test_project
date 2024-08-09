"""id primary kay two

Revision ID: 29f7d8017082
Revises: 7b0180c31188
Create Date: 2024-08-09 18:02:04.080444

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '29f7d8017082'
down_revision: Union[str, None] = '7b0180c31188'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Usando o batch mode para SQLite
    with op.batch_alter_table('users', schema=None) as batch_op:
        # Remover a constraint de chave primária antiga
        batch_op.drop_constraint('pk_users_cpf', type_='primary')
        # Adicionar a nova chave primária
        batch_op.create_primary_key('users_pkey', ['id'])

def downgrade() -> None:
    # Usando o batch mode para SQLite
    with op.batch_alter_table('users', schema=None) as batch_op:
        # Remover a constraint de chave primária existente
        batch_op.drop_constraint('users_pkey', type_='primary')
        # Recriar a chave primária antiga
        batch_op.create_primary_key('pk_users_cpf', ['cpf'])
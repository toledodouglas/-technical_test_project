"""refactor

Revision ID: 7b0180c31188
Revises: 96a0304b8280
Create Date: 2024-08-09 17:55:30.868892

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '7b0180c31188'
down_revision: Union[str, None] = '96a0304b8280'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    # Usando batch mode para garantir compatibilidade com SQLite
    with op.batch_alter_table('users') as batch_op:
        # Adicionar a coluna 'id' como chave primária
        batch_op.add_column(sa.Column('id', sa.Integer, autoincrement=True, primary_key=True))
        
        # Remover a constraint de unicidade da coluna 'cpf'
        batch_op.drop_constraint('uq_users_cpf', type_='unique')
        
        # Adicionar a nova coluna 'uf'
        batch_op.add_column(sa.Column('uf', sa.String(), nullable=False))
        
        # Remover a coluna 'password'
        batch_op.drop_column('password')

def downgrade() -> None:
    # Usando batch mode para garantir compatibilidade com SQLite
    with op.batch_alter_table('users') as batch_op:
        # Adicionar a coluna 'password' de volta
        batch_op.add_column(sa.Column('password', sa.VARCHAR(), nullable=False))
        
        # Adicionar a constraint de unicidade de volta para 'cpf'
        batch_op.create_unique_constraint('uq_users_cpf', ['cpf'])
        
        # Remover a coluna 'id'
        batch_op.drop_column('id')
        
        # Remover a coluna 'uf'
        batch_op.drop_column('uf')
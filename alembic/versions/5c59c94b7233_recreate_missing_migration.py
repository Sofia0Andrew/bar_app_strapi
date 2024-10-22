"""Recreate missing migration

Revision ID: 5c59c94b7233
Revises: 
Create Date: 2024-10-21 17:47:34.815136

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b537a038e8b7'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Удаление таблицы drink_bar
    op.drop_table('drink_bar')

    # Добавление поля bar_id в таблицу drinks
    op.add_column('drinks', sa.Column('bar_id', sa.Integer(), sa.ForeignKey('bars.id'), nullable=True))

def downgrade():
    # Отмена добавления поля bar_id в таблицу drinks
    op.drop_column('drinks', 'bar_id')

    # Восстановление таблицы drink_bar
    op.create_table(
        'drink_bar',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('drink_id', sa.Integer(), sa.ForeignKey('drinks.id'), nullable=False),
        sa.Column('bar_id', sa.Integer(), sa.ForeignKey('bars.id'), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
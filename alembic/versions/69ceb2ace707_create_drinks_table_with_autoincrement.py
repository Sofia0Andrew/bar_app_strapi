"""Create drinks table with autoincrement

Revision ID: 69ceb2ace707
Revises: b537a038e8b7
Create Date: 2024-10-21 18:04:55.915135

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '69ceb2ace707'
down_revision: Union[str, None] = 'b537a038e8b7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'drinks',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('drinkName', sa.String(), nullable=True),
        sa.Column('price', sa.Numeric(precision=10, scale=2), nullable=True),
        sa.Column('drinkType', sa.String(), nullable=True),
        sa.Column('recipe', sa.String(), nullable=True),
        sa.Column('stock', sa.Boolean(), nullable=True, server_default='True'),
        sa.Column('bar_id', sa.Integer(), sa.ForeignKey('bars.id'), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_drinks_drinkName'), 'drinks', ['drinkName'], unique=False)
    op.create_index(op.f('ix_drinks_id'), 'drinks', ['id'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_drinks_id'), table_name='drinks')
    op.drop_index(op.f('ix_drinks_drinkName'), table_name='drinks')
    op.drop_table('drinks')

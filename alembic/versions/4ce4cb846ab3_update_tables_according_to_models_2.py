"""Update tables according to models 2

Revision ID: 4ce4cb846ab3
Revises: 5724d93acf18
Create Date: 2024-10-21 21:37:16.732023

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '4ce4cb846ab3'
down_revision: Union[str, None] = '5724d93acf18'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('username', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('password_', sa.String(), nullable=False),
        sa.Column('confirmed', sa.Boolean(), nullable=False, server_default='False'),
        sa.Column('blocked_', sa.Boolean(), nullable=False, server_default='False'),
        sa.Column('roles', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=False)

    op.create_table(
        'bars',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('address', sa.String(), nullable=False),
        sa.Column('working_time_start', sa.Time(), nullable=False),
        sa.Column('working_time_finish', sa.Time(), nullable=False),
        sa.Column('description', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_bars_id'), 'bars', ['id'], unique=False)
    op.create_index(op.f('ix_bars_name'), 'bars', ['name'], unique=False)

    op.create_table(
        'managers',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('fullName', sa.String(), nullable=False),
        sa.Column('phoneNumber', sa.String(length=11), nullable=False),
        sa.Column('bar_id', sa.Integer(), sa.ForeignKey('bars.id'), nullable=False),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id'), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('phoneNumber')
    )
    op.create_index(op.f('ix_managers_id'), 'managers', ['id'], unique=False)
    op.create_index(op.f('ix_managers_fullName'), 'managers', ['fullName'], unique=False)

    op.create_table(
        'barmen',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('fullName', sa.String(), nullable=False),
        sa.Column('phoneNumber', sa.String(length=11), nullable=False),
        sa.Column('bar_id', sa.Integer(), sa.ForeignKey('bars.id'), nullable=False),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id'), nullable=False),
        sa.Column('manager_id', sa.Integer(), sa.ForeignKey('managers.id'), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('phoneNumber')
    )
    op.create_index(op.f('ix_barmen_id'), 'barmen', ['id'], unique=False)
    op.create_index(op.f('ix_barmen_fullName'), 'barmen', ['fullName'], unique=False)

    op.create_table(
        'drinks',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('drinkName', sa.String(), nullable=False),
        sa.Column('price', sa.Numeric(precision=10, scale=2), nullable=False),
        sa.Column('drinkType', sa.String(), nullable=False),
        sa.Column('recipe', sa.String(), nullable=False),
        sa.Column('stock', sa.Boolean(), nullable=False, server_default='True'),
        sa.Column('bar_id', sa.Integer(), sa.ForeignKey('bars.id'), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_drinks_id'), 'drinks', ['id'], unique=False)
    op.create_index(op.f('ix_drinks_drinkName'), 'drinks', ['drinkName'], unique=False)

def downgrade():
    op.drop_index(op.f('ix_drinks_drinkName'), table_name='drinks')
    op.drop_index(op.f('ix_drinks_id'), table_name='drinks')
    op.drop_table('drinks')
    op.drop_index(op.f('ix_barmen_fullName'), table_name='barmen')
    op.drop_index(op.f('ix_barmen_id'), table_name='barmen')
    op.drop_table('barmen')
    op.drop_index(op.f('ix_managers_fullName'), table_name='managers')
    op.drop_index(op.f('ix_managers_id'), table_name='managers')
    op.drop_table('managers')
    op.drop_index(op.f('ix_bars_name'), table_name='bars')
    op.drop_index(op.f('ix_bars_id'), table_name='bars')
    op.drop_table('bars')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_table('users')

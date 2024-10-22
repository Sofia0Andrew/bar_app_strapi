"""add access_token to user model

Revision ID: fe53f51d9097
Revises: 332256f518eb
Create Date: 2024-10-22 00:55:09.818106

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'fe53f51d9097'
down_revision: Union[str, None] = '332256f518eb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('access_token', sa.String(), nullable=True))
    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'access_token')
    # ### end Alembic commands ###

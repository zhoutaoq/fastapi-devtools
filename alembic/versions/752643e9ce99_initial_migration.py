"""initial migration

Revision ID: 752643e9ce99
Revises: 
Create Date: 2024-08-22 16:54:12.672063

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '752643e9ce99'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_user_profiles_id', table_name='user_profiles')
    op.drop_table('user_profiles')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_profiles',
    sa.Column('id', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('create_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('update_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('avatar_url', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('nickname', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('birth_date', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('bio', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='user_profiles_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='user_profiles_pkey')
    )
    op.create_index('ix_user_profiles_id', 'user_profiles', ['id'], unique=True)
    # ### end Alembic commands ###
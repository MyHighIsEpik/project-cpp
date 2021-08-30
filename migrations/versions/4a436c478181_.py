"""empty message

Revision ID: 4a436c478181
Revises: 03548f7c9c56
Create Date: 2021-08-20 00:44:27.932605

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a436c478181'
down_revision = '03548f7c9c56'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('gameinfo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('cpu', sa.Text(), nullable=True),
    sa.Column('ram', sa.Integer(), nullable=True),
    sa.Column('osversion', sa.Text(), nullable=True),
    sa.Column('videocard', sa.Text(), nullable=True),
    sa.Column('diskspace', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('name', name=op.f('pk_gameinfo'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('gameinfo')
    # ### end Alembic commands ###

"""empty message

Revision ID: c478387b0af8
Revises: 4a436c478181
Create Date: 2021-08-20 00:45:12.099057

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c478387b0af8'
down_revision = '4a436c478181'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('illustinfo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('cpu', sa.Text(), nullable=True),
    sa.Column('ram', sa.Integer(), nullable=True),
    sa.Column('osversion', sa.Text(), nullable=True),
    sa.Column('videocard', sa.Text(), nullable=True),
    sa.Column('diskspace', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('name', name=op.f('pk_illustinfo'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('illustinfo')
    # ### end Alembic commands ###

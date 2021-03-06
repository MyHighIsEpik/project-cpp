"""empty message

Revision ID: d7227368475c
Revises: f13bd1ebe783
Create Date: 2021-11-02 02:23:20.278347

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd7227368475c'
down_revision = 'f13bd1ebe783'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index('uq_user_email')
        batch_op.create_unique_constraint(batch_op.f('uq_user_codenum'), ['codenum'])
        batch_op.create_unique_constraint(batch_op.f('uq_user_nickname'), ['nickname'])

    with op.batch_alter_table('user_pcinfo', schema=None) as batch_op:
        batch_op.create_foreign_key(batch_op.f('fk_user_pcinfo_codenum_user'), 'user', ['codenum'], ['codenum'], ondelete='CASCADE')

    with op.batch_alter_table('videocard', schema=None) as batch_op:
        batch_op.alter_column('vcname',
               existing_type=mysql.TEXT(),
               nullable=False)
        batch_op.alter_column('score',
               existing_type=mysql.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('videocard', schema=None) as batch_op:
        batch_op.alter_column('score',
               existing_type=mysql.INTEGER(),
               nullable=True)
        batch_op.alter_column('vcname',
               existing_type=mysql.TEXT(),
               nullable=True)

    with op.batch_alter_table('user_pcinfo', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_user_pcinfo_codenum_user'), type_='foreignkey')

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_user_nickname'), type_='unique')
        batch_op.drop_constraint(batch_op.f('uq_user_codenum'), type_='unique')
        batch_op.create_index('uq_user_email', ['nickname'], unique=False)

    # ### end Alembic commands ###

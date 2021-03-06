"""empty message

Revision ID: 16a4a2b43664
Revises: d7227368475c
Create Date: 2021-11-02 02:25:07.111174

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '16a4a2b43664'
down_revision = 'd7227368475c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_codenum', sa.String(length=45), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_question_user_codenum_user_pcinfo'), 'user_pcinfo', ['user_codenum'], ['codenum'], ondelete='CASCADE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_question_user_codenum_user_pcinfo'), type_='foreignkey')
        batch_op.drop_column('user_codenum')

    # ### end Alembic commands ###

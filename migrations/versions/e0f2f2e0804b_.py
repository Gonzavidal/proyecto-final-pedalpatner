"""empty message

Revision ID: e0f2f2e0804b
Revises: bbb2bb632aba
Create Date: 2023-05-09 04:33:59.225697

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e0f2f2e0804b'
down_revision = 'bbb2bb632aba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comunicacion', schema=None) as batch_op:
        batch_op.add_column(sa.Column('imagen', sa.String(length=250), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comunicacion', schema=None) as batch_op:
        batch_op.drop_column('imagen')

    # ### end Alembic commands ###

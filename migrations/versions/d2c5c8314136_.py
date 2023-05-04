"""empty message

Revision ID: d2c5c8314136
Revises: c16f85903662
Create Date: 2023-04-27 17:54:58.897112

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd2c5c8314136'
down_revision = 'c16f85903662'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('direccion',
               existing_type=sa.VARCHAR(length=220),
               type_=sa.String(length=230),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('direccion',
               existing_type=sa.String(length=230),
               type_=sa.VARCHAR(length=220),
               existing_nullable=False)

    # ### end Alembic commands ###
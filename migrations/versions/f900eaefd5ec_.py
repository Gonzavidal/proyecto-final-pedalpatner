"""empty message

Revision ID: f900eaefd5ec
Revises: d2c5c8314136
Create Date: 2023-05-03 20:15:48.785246

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f900eaefd5ec'
down_revision = 'd2c5c8314136'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comunicacion', schema=None) as batch_op:
        batch_op.alter_column('titulo',
               existing_type=sa.VARCHAR(length=130),
               type_=sa.String(length=140),
               existing_nullable=False)
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(length=100),
               type_=sa.String(length=110),
               existing_nullable=False)
        batch_op.alter_column('tipos_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    with op.batch_alter_table('talleres', schema=None) as batch_op:
        batch_op.drop_constraint('talleres_users_id_fkey', type_='foreignkey')
        batch_op.drop_column('users_id')

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=390),
               type_=sa.String(length=400),
               existing_nullable=False)
        batch_op.alter_column('direccion',
               existing_type=sa.VARCHAR(length=230),
               type_=sa.String(length=220),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('direccion',
               existing_type=sa.String(length=220),
               type_=sa.VARCHAR(length=230),
               existing_nullable=False)
        batch_op.alter_column('password',
               existing_type=sa.String(length=400),
               type_=sa.VARCHAR(length=390),
               existing_nullable=False)

    with op.batch_alter_table('talleres', schema=None) as batch_op:
        batch_op.add_column(sa.Column('users_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.create_foreign_key('talleres_users_id_fkey', 'users', ['users_id'], ['id'])

    with op.batch_alter_table('comunicacion', schema=None) as batch_op:
        batch_op.alter_column('tipos_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('email',
               existing_type=sa.String(length=110),
               type_=sa.VARCHAR(length=100),
               existing_nullable=False)
        batch_op.alter_column('titulo',
               existing_type=sa.String(length=140),
               type_=sa.VARCHAR(length=130),
               existing_nullable=False)

    # ### end Alembic commands ###
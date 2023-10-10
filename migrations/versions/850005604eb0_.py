"""empty message

Revision ID: 850005604eb0
Revises: 
Create Date: 2023-10-09 18:24:51.898460

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '850005604eb0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('schedule',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('d1_morning', sa.String(length=128), nullable=True),
    sa.Column('d1_afternoon', sa.String(length=128), nullable=True),
    sa.Column('d1_evening', sa.String(length=128), nullable=True),
    sa.Column('d2_morning', sa.String(length=128), nullable=True),
    sa.Column('d2_afternoon', sa.String(length=128), nullable=True),
    sa.Column('d2_evening', sa.String(length=128), nullable=True),
    sa.Column('d3_morning', sa.String(length=128), nullable=True),
    sa.Column('d3_afternoon', sa.String(length=128), nullable=True),
    sa.Column('d3_evening', sa.String(length=128), nullable=True),
    sa.Column('d4_morning', sa.String(length=128), nullable=True),
    sa.Column('d4_afternoon', sa.String(length=128), nullable=True),
    sa.Column('d4_evening', sa.String(length=128), nullable=True),
    sa.Column('d5_morning', sa.String(length=128), nullable=True),
    sa.Column('d5_afternoon', sa.String(length=128), nullable=True),
    sa.Column('d5_evening', sa.String(length=128), nullable=True),
    sa.Column('d6_morning', sa.String(length=128), nullable=True),
    sa.Column('d6_afternoon', sa.String(length=128), nullable=True),
    sa.Column('d6_evening', sa.String(length=128), nullable=True),
    sa.Column('d7_morning', sa.String(length=128), nullable=True),
    sa.Column('d7_afternoon', sa.String(length=128), nullable=True),
    sa.Column('d7_evening', sa.String(length=128), nullable=True),
    sa.Column('week', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('staff',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('gender', sa.String(length=16), nullable=False),
    sa.Column('birthyear', sa.Integer(), nullable=False),
    sa.Column('workyear', sa.Integer(), nullable=False),
    sa.Column('daylike', sa.String(length=128), nullable=True),
    sa.Column('timelike', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=128), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.Column('is_staff', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('staff')
    op.drop_table('schedule')
    # ### end Alembic commands ###

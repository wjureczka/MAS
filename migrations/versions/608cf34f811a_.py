"""empty message

Revision ID: 608cf34f811a
Revises: ed4b590d34d7
Create Date: 2020-06-17 19:27:34.653325

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '608cf34f811a'
down_revision = 'ed4b590d34d7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rental_object',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('area_description', sa.String(length=200), nullable=True),
    sa.Column('equipment', sa.String(length=200), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('flat',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['rental_object.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('opinion',
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.Column('rental_object_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['tenant.id'], ),
    sa.ForeignKeyConstraint(['rental_object_id'], ['rental_object.id'], ),
    sa.PrimaryKeyConstraint('author_id', 'rental_object_id')
    )
    op.create_table('room',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('flat_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['flat_id'], ['flat.id'], ),
    sa.ForeignKeyConstraint(['id'], ['rental_object.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('room')
    op.drop_table('opinion')
    op.drop_table('flat')
    op.drop_table('rental_object')
    # ### end Alembic commands ###

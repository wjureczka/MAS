"""empty message

Revision ID: 96110a91786e
Revises: 608cf34f811a
Create Date: 2020-06-17 19:30:25.676991

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96110a91786e'
down_revision = '608cf34f811a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('opinion', sa.Column('comment', sa.String(length=200), nullable=True))
    op.add_column('opinion', sa.Column('rate', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('opinion', 'rate')
    op.drop_column('opinion', 'comment')
    # ### end Alembic commands ###

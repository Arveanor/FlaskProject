"""followers

Revision ID: 8680e0ec3528
Revises: 93c4305acd77
Create Date: 2019-01-19 00:02:47.455203

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8680e0ec3528'
down_revision = '93c4305acd77'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###

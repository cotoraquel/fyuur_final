"""empty message

Revision ID: 1ed2be378efa
Revises: 3e63d0c73a01
Create Date: 2023-07-25 02:32:57.990173

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1ed2be378efa'
down_revision = '3e63d0c73a01'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('venues', schema=None) as batch_op:
        batch_op.add_column(sa.Column('city_name', sa.String(length=120), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('venues', schema=None) as batch_op:
        batch_op.drop_column('city_name')

    # ### end Alembic commands ###

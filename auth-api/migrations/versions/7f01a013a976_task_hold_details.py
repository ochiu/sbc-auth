"""task hold details

Revision ID: 7f01a013a976
Revises: 886fa2608e93
Create Date: 2021-06-09 13:42:21.424303

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f01a013a976'
down_revision = '886fa2608e93'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('remarks', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tasks', 'remarks')
    # ### end Alembic commands ###

"""empty message

Revision ID: 94be73a0b2af
Revises: 
Create Date: 2022-07-02 10:55:42.195649

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '94be73a0b2af'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'employees', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'employees', type_='unique')
    # ### end Alembic commands ###

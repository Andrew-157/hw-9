"""INIT

Revision ID: 572c5e5678b9
Revises: 
Create Date: 2022-11-29 15:36:37.856277

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '572c5e5678b9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contacts',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('phones',
    sa.Column('contact_id', sa.Integer(), nullable=True),
    sa.Column('phone', sa.String(length=15), nullable=False),
    sa.ForeignKeyConstraint(['contact_id'], ['contacts.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('phone')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('phones')
    op.drop_table('contacts')
    # ### end Alembic commands ###
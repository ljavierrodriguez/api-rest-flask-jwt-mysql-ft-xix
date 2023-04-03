"""empty message

Revision ID: a286bd72ca49
Revises: 
Create Date: 2023-04-03 14:36:25.645484

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a286bd72ca49'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('roles',
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('users',
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=120), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('messages',
    sa.Column('message', sa.Text(), nullable=False),
    sa.Column('from_id', sa.Integer(), nullable=False),
    sa.Column('to_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['from_id'], ['users.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['to_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('profiles',
    sa.Column('bio', sa.Text(), nullable=True),
    sa.Column('facebook', sa.String(length=120), nullable=True),
    sa.Column('twitter', sa.String(length=120), nullable=True),
    sa.Column('instagram', sa.String(length=120), nullable=True),
    sa.Column('github', sa.String(length=120), nullable=True),
    sa.Column('linkedin', sa.String(length=120), nullable=True),
    sa.Column('users_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['users_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('users_id')
    )
    op.create_table('roles_users',
    sa.Column('roles_id', sa.Integer(), nullable=False),
    sa.Column('users_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['roles_id'], ['roles.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['users_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('roles_id', 'users_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('roles_users')
    op.drop_table('profiles')
    op.drop_table('messages')
    op.drop_table('users')
    op.drop_table('roles')
    # ### end Alembic commands ###

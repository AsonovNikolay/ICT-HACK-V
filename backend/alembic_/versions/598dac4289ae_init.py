"""init

Revision ID: 598dac4289ae
Revises: 
Create Date: 2022-12-12 14:24:49.919223

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '598dac4289ae'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('administrator',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.String(length=30), nullable=True),
    sa.Column('last_name', sa.String(length=30), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_index(op.f('ix_administrator_id'), 'administrator', ['id'], unique=False)
    op.create_table('organization',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('contacts', sa.String(), nullable=True),
    sa.Column('approved', sa.Boolean(), nullable=True),
    sa.Column('specialization', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_organization_id'), 'organization', ['id'], unique=False)
    op.create_table('student',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.String(length=30), nullable=True),
    sa.Column('last_name', sa.String(length=30), nullable=True),
    sa.Column('bio', sa.String(), nullable=True),
    sa.Column('education', sa.String(), nullable=True),
    sa.Column('hard_soft_skills', sa.String(), nullable=True),
    sa.Column('projects', sa.String(), nullable=True),
    sa.Column('telegram', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('phone_number', sa.String(), nullable=True),
    sa.Column('linkedin', sa.String(), nullable=True),
    sa.Column('site', sa.String(), nullable=True),
    sa.Column('specialization', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('linkedin'),
    sa.UniqueConstraint('phone_number'),
    sa.UniqueConstraint('telegram')
    )
    op.create_index(op.f('ix_student_id'), 'student', ['id'], unique=False)
    op.create_table('administrator_token',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('token', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('expire_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['administrator.id'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_administrator_token_id'), 'administrator_token', ['id'], unique=False)
    op.create_table('organization_token',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('token', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('expire_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['organization.id'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_organization_token_id'), 'organization_token', ['id'], unique=False)
    op.create_table('pet_project',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['student_id'], ['student.id'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_pet_project_id'), 'pet_project', ['id'], unique=False)
    op.create_table('position',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('requirements', sa.String(), nullable=True),
    sa.Column('organization_id', sa.Integer(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('salary', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['organization_id'], ['organization.id'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_position_id'), 'position', ['id'], unique=False)
    op.create_table('student_token',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('token', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('expire_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['student.id'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_student_token_id'), 'student_token', ['id'], unique=False)
    op.create_table('project_member',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('pet_project_id', sa.Integer(), nullable=True),
    sa.Column('role', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['pet_project_id'], ['pet_project.id'], ondelete='cascade'),
    sa.ForeignKeyConstraint(['user_id'], ['student.id'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_project_member_id'), 'project_member', ['id'], unique=False)
    op.create_table('student_response',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('pet_project_id', sa.Integer(), nullable=True),
    sa.Column('message', sa.String(), nullable=True),
    sa.Column('accepted', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['pet_project_id'], ['pet_project.id'], ondelete='cascade'),
    sa.ForeignKeyConstraint(['user_id'], ['student.id'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_student_response_id'), 'student_response', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_student_response_id'), table_name='student_response')
    op.drop_table('student_response')
    op.drop_index(op.f('ix_project_member_id'), table_name='project_member')
    op.drop_table('project_member')
    op.drop_index(op.f('ix_student_token_id'), table_name='student_token')
    op.drop_table('student_token')
    op.drop_index(op.f('ix_position_id'), table_name='position')
    op.drop_table('position')
    op.drop_index(op.f('ix_pet_project_id'), table_name='pet_project')
    op.drop_table('pet_project')
    op.drop_index(op.f('ix_organization_token_id'), table_name='organization_token')
    op.drop_table('organization_token')
    op.drop_index(op.f('ix_administrator_token_id'), table_name='administrator_token')
    op.drop_table('administrator_token')
    op.drop_index(op.f('ix_student_id'), table_name='student')
    op.drop_table('student')
    op.drop_index(op.f('ix_organization_id'), table_name='organization')
    op.drop_table('organization')
    op.drop_index(op.f('ix_administrator_id'), table_name='administrator')
    op.drop_table('administrator')
    # ### end Alembic commands ###

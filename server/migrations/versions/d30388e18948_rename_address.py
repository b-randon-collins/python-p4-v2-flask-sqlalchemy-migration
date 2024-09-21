"""rename address

Revision ID: d30388e18948
Revises: e50e0750947f
Create Date: 2024-09-21 06:56:00.431350

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd30388e18948'
down_revision = 'e50e0750947f'
branch_labels = None
depends_on = None


def upgrade():
    # Rename the column 'address' to 'location'
    op.alter_column('departments', 'address', new_column_name='location')

def downgrade():
    # Rename the column 'location' back to 'address'
    op.alter_column('departments', 'location', new_column_name='address')

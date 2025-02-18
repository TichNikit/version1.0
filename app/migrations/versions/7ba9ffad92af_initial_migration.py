"""Initial migration

Revision ID: 7ba9ffad92af
Revises: 2f20efb24e25
Create Date: 2024-10-20 18:43:03.271745

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7ba9ffad92af'
down_revision: Union[str, None] = '2f20efb24e25'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_user_game_feedback_id', table_name='user_game_feedback')
    op.drop_table('user_game_feedback')
    op.drop_index('ix_user_game_ratings_id', table_name='user_game_ratings')
    op.drop_table('user_game_ratings')
    op.add_column('games', sa.Column('feedback', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('games', 'feedback')
    op.create_table('user_game_ratings',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.Column('game_id', sa.INTEGER(), nullable=True),
    sa.Column('rating', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['game_id'], ['games.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_user_game_ratings_id', 'user_game_ratings', ['id'], unique=False)
    op.create_table('user_game_feedback',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.Column('game_id', sa.INTEGER(), nullable=True),
    sa.Column('feedback', sa.VARCHAR(), nullable=True),
    sa.ForeignKeyConstraint(['game_id'], ['games.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_user_game_feedback_id', 'user_game_feedback', ['id'], unique=False)
    # ### end Alembic commands ###

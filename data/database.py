import datetime
import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Phrases(SqlAlchemyBase):
    __tablename__ = 'phrases'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    phrase = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    author = sqlalchemy.Column(sqlalchemy.String, nullable=True)


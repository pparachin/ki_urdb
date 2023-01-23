from app import db
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Column, Integer, Table, String, DateTime
from authors.models import Authors


class Albums(db.Model):
    id_a = Column(Integer, primary_key=True)
    title = Column(String(64), nullable=False)
    release_year = Column(Integer, nullable=False)
    number_of_songs = Column(Integer, nullable=False)
    length_sec = Column(Integer, nullable=False)
    author_id = Column(Integer, ForeignKey(Authors.id_a, ondelete="CASCADE"))
    author = relationship(Authors, cascade='save-update, merge, delete')
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)


def get_id():
    return Albums.id_a

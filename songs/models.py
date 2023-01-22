from app import db
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Column, Integer, Table, String, DateTime
from albums.models import Albums


class Genres(db.Model):
    id_g = Column(Integer, primary_key=True)
    title = Column(String(32), nullable=False)
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)


class Songs(db.Model):
    id_s = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    genre_id = Column(Integer, ForeignKey("genres.id_g"))
    genre = relationship("Genres")
    length = Column(Integer, nullable=False)
    number_of_plays = Column(Integer, nullable=False)
    album_id = Column(Integer, ForeignKey("albums.id_a"))
    album = relationship("Albums")
    release_year = Column(Integer, nullable=True)
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)

    def __repr__(self):
        return f'<Song {self.id_s} {self.name}>'
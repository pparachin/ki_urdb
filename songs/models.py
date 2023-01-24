from app import db
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Column, Integer, Table, String, DateTime
from albums.models import Albums


class Songs(db.Model):
    id_s = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    genre_id = Column(db.Integer, db.ForeignKey('genres.id_g'), nullable=False)
    genre = relationship("Genres", lazy="select", backref=db.backref('Genres', lazy='joined'))
    length = Column(Integer, nullable=False)
    number_of_plays = Column(Integer, nullable=False)
    album_id = db.Column(db.Integer, db.ForeignKey(Albums.id_a), nullable=True)
    album = db.relationship('Albums', lazy='select', backref=db.backref('Albums', lazy='joined'))
    release_year = Column(Integer, nullable=True)
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)

    def __repr__(self):
        return f'<Song {self.id_s} {self.name}>'
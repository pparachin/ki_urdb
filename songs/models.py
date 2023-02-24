from app import db
from sqlalchemy.orm import relationship
from albums.models import Albums


class Songs(db.Model):
    id_s = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id_g'), nullable=False)
    genre = db.relationship("Genres", lazy="select", backref=db.backref('Genres', lazy='joined'))
    length = db.Column(db.Integer, nullable=False)
    number_of_plays = db.Column(db.Integer, nullable=False)
    album_id = db.Column(db.Integer, db.ForeignKey(Albums.id_a), nullable=True)
    album = db.relationship('Albums', lazy='select', backref=db.backref('Albums', lazy='joined'))
    release_year = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime, nullable=True)
    updated_at = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f'<Song {self.id_s} {self.name}>'
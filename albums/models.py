from app import db
from authors.models import Authors


class Albums(db.Model):
    id_a = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    release_year = db.Column(db.Integer, nullable=False)
    number_of_songs = db.Column(db.Integer, nullable=False)
    length_sec = db.Column(db.Integer, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey(Authors.id_a), nullable=True)
    author = db.relationship('Authors', lazy='select', backref=db.backref('Authors', lazy='joined'))
    created_at = db.Column(db.DateTime, nullable=True)
    updated_at = db.Column(db.DateTime, nullable=True)


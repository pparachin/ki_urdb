from app import db


class Genres(db.Model):
    id_g = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), nullable=False)
    created_at = db.Column(db.DateTime, nullable=True)
    updated_at = db.Column(db.DateTime, nullable=True)
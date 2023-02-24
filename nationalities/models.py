from app import db


class Nationalities(db.Model):
    id_n = db.Column(db.Integer, primary_key=True)
    nationality = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, nullable=True)
    updated_at = db.Column(db.DateTime, nullable=True)
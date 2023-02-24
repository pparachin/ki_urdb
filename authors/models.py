from app import db
from sqlalchemy.orm import relationship


class Authors(db.Model):
    id_a = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    nationality_id = db.Column(db.Integer, db.ForeignKey('nationalities.id_n'), nullable=False)
    nationality = relationship("Nationalities", lazy="select", backref=db.backref('Nationalities', lazy='joined'))
    number_of_songs = db.Column(db.Integer, nullable=False)
    number_of_albums = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=True)
    updated_at = db.Column(db.DateTime, nullable=True)

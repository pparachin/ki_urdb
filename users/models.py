from app import db


class Users(db.Model):
    id_u = db.Column(db.Integer, primary_key=True)
    profile_name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    date_of_birth = db.Column(db.DateTime, nullable=False)
    gender = db.Column(db.Integer, db.ForeignKey('genders.id_g'), nullable=False)
    gender_f = db.relationship("Genders", lazy="select", backref=db.backref("Genders", lazy="joined"))
    created_at = db.Column(db.DateTime, nullable=True)
    updated_at = db.Column(db.DateTime, nullable=True)


class Genders(db.Model):
    id_g = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False)
    description = db.Column(db.String(100), nullable=False)
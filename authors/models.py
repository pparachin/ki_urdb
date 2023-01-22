from app import db
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Column, Integer, Table, String, DateTime


class Nationalities(db.Model):
    id_n = Column(Integer, primary_key=True)
    nationality = Column(String(128), nullable=False)


class Authors(db.Model):
    id_a = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    nationality_id = Column(Integer, ForeignKey('nationalities.id_n'))
    nationality = relationship('Nationalities')
    number_of_songs = Column(Integer, nullable=False)
    number_of_albums = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)
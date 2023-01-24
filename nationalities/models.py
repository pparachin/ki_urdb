from app import db
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Column, Integer, Table, String, DateTime


class Nationalities(db.Model):
    id_n = Column(Integer, primary_key=True)
    nationality = Column(String(128), nullable=False)
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)
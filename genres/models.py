from app import db
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Column, Integer, Table, String, DateTime
from albums.models import Albums


class Genres(db.Model):
    id_g = Column(Integer, primary_key=True)
    title = Column(String(32), nullable=False)
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)
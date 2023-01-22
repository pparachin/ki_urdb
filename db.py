from config import MYSQL_DB, MYSQL_USER, MYSQL_HOST
from sqlalchemy import create_engine

engine = create_engine(f"mysql://{MYSQL_USER}@{MYSQL_HOST}/{MYSQL_DB}")

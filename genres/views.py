from flask import (render_template)
from genres import bp
from app import db
from genres.models import Genres


@bp.route("/")
def index_view():
    genres = db.paginate(db.select(Genres).order_by(Genres.id_g), per_page=10)

    return render_template("genres/index.html", genres=genres, title="SQLAlchemyORM - Genres")

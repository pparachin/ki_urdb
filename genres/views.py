import datetime

from flask import (render_template, request, url_for, redirect, flash)
from genres import bp
from genres.models import Genres


@bp.route("/")
def index_view():
    page = request.args.get('page', 1, type=int)
    genres = Genres.query.paginate(page=page, per_page=10)

    return render_template("genres/index.html", genres=genres)
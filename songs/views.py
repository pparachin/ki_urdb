from flask import (render_template, request, url_for, redirect, flash)

from songs import bp

from songs.models import Songs


@bp.route("/")
def index_view():
    page = request.args.get('page', 1, type=int)

    songs = Songs.query.paginate(page=page, per_page=10)

    return render_template("songs/index.html", songs=songs)
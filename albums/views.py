from flask import (render_template, request, url_for, redirect, flash)
from sqlalchemy import update
from albums import bp
from app import db

from albums.models import Albums
from albums.models import Authors


@bp.route("/")
def index_view():
    page = request.args.get('page', 1, type=int)

    albums = Albums.query.paginate(page=page, per_page=10)

    return render_template("albums/index.html", albums=albums)


@bp.route("/edit/<id>", methods=["POST", "GET"])
def update_view(id):
    if not id:
        return redirect(url_for("albums.index_view"))
    try:
        album = Albums.query.get(id)
        authors = Authors.query.all()
    except Exception:
        flash("This album does not exist", "error")
        return redirect(url_for("albums.index_view"))

    if request.method == "POST":
        album.title = request.form["title"]
        album.release_year = request.form["release_year"]
        album.number_of_songs = request.form["number_of_songs"]
        album.length_sec = request.form["length_sec"]
        album.author_id = request.form["author"]

        new_album = Albums(title=request.form["title"],release_year=request.form["release_year"],number_of_songs=request.form["number_of_songs"],length_sec=request.form["length_sec"],author_id=request.form["author"])
        album.add(new_album)

        flash("Album updated", "success")
        return redirect(url_for("albums.index_view"))


    return render_template("albums/update.html", album=album, authors=authors)
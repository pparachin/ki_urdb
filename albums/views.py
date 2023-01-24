import datetime

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
        album.updated_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        album.verified = True
        db.session.add(album)
        db.session.commit()

        flash("Album updated", "success")
        return redirect(url_for("albums.index_view"))

    return render_template("albums/update.html", album=album, authors=authors)


@bp.route("/delete/<id>", methods=["POST", "DELETE"])
def delete_record(id):
    if not id:
        return redirect(url_for("albums.index_view"))
    try:
        album = Albums.query.get(id)
    except Exception:
        flash("This album does not exist", "error")
        return redirect(url_for("albums.index_view"))

    if request.method == "POST":
        db.session.delete(album)
        print(album.id_a)
        db.session.commit()
        flash('Album was successfully deleted from database', 'error')
        return redirect(url_for("albums.index_view"))


@bp.route("/add", methods=["POST", "GET"])
def add_view():
    if request.method == "POST":
        album_title = request.form["title"]
        album_release_year = request.form["release_year"]
        album_number_of_songs = request.form["number_of_songs"]
        album_length_sec = request.form["length_sec"]
        album_author_id = request.form["author"]
        album_created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        album_updated_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        album = Albums(title=album_title, release_year=album_release_year, number_of_songs=album_number_of_songs, length_sec=album_length_sec, author_id=album_author_id, created_at=album_created_at, updated_at=album_updated_at)

        db.session.add(album)
        db.session.commit()

        flash("Album was successfully added to database!", "success")
        return redirect(url_for("albums.index_view"))

    else:
        authors = Authors.query.all()
        albums = Albums.query.all()
        return render_template("albums/add.html", albums=albums, authors=authors)
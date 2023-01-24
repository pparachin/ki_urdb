import datetime

from flask import (render_template, request, url_for, redirect, flash)

from songs import bp

from songs.models import Songs
from genres.models import Genres
from albums.models import Albums
from app import db


@bp.route("/")
def index_view():
    page = request.args.get('page', 1, type=int)

    songs = Songs.query.paginate(page=page, per_page=10)

    return render_template("songs/index.html", songs=songs)


@bp.route("/edit/<id>", methods=["POST", "GET"])
def update_view(id):
    if not id:
        return redirect(url_for("songs.index_view"))
    try:
        song = Songs.query.get(id)
        genres = Genres.query.all()
        albums = Albums.query.all()
    except Exception:
        flash("This song does not exist", "error")
        return redirect(url_for("songs.index_view"))

    if request.method == "POST":
        song.name = request.form["name"]
        song.genre_id = request.form["genre"]
        song.length = request.form["length"]
        song.number_of_plays = request.form["number_of_plays"]
        song.album_id = request.form["album"]
        song.release_year = request.form["release_year"]
        song.updated_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        song.verified = True
        db.session.add(song)
        db.session.commit()

        flash("Song updated", "success")
        return redirect(url_for("songs.index_view"))

    return render_template("songs/update.html", song=song, albums=albums, genres=genres)


@bp.route("/add", methods=["POST", "GET"])
def add_view():
    if request.method == "POST":
        song_name = request.form["name"]
        song_genre_id = request.form["genre"]
        song_length = request.form["length"]
        song_number_plays = request.form["number_of_plays"]
        song_album_id = request.form["album"]
        song_release_year = request.form["release_year"]
        song_created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        song_updated_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if song_album_id == "NULL":
            song = Songs(name=song_name, genre_id=song_genre_id, length=song_length, number_of_plays=song_number_plays, release_year=song_release_year, created_at=song_created_at ,updated_at=song_updated_at)
        else:
            song = Songs(name=song_name, genre_id=song_genre_id, length=song_length, number_of_plays=song_number_plays, album_id=song_album_id,release_year=song_release_year, created_at=song_created_at ,updated_at=song_updated_at)

        db.session.add(song)
        db.session.commit()

        flash("Song was successfully added to database!", "success")
        return redirect(url_for("songs.index_view"))

    else:
        genres = Genres.query.all()
        albums = Albums.query.all()
        return render_template("songs/add.html", albums=albums, genres=genres)


@bp.route("/delete/<id>", methods=["POST", "DELETE"])
def delete_record(id):
    if not id:
        return redirect(url_for("songs.index_view"))
    try:
        song = Songs.query.get(id)
    except Exception:
        flash("This song does not exist", "error")
        return redirect(url_for("songs.index_view"))

    if request.method == "POST":
        db.session.delete(song)
        print(song.id_s)
        db.session.commit()
        flash("Song was successfully deleted from database", "success")
        return redirect(url_for("songs.index_view"))
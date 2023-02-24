import datetime

from flask import (render_template, request, url_for, redirect, flash)
from albums import bp
from app import db
from albums.models import Albums
from albums.models import Authors


@bp.route("/")
def index_view():
    albums = db.paginate(db.select(Albums).order_by(Albums.id_a), per_page=10)

    return render_template("albums/index.html", albums=albums, title="SQLAlchemyORM - Albums")


@bp.route("/edit/<id>", methods=["POST", "GET"])
def update_view(id):
    if not id:
        return redirect(url_for("albums.index_view"))
    try:
        album = db.session.execute(db.select(Albums).filter_by(id_a=id)).first()
        authors = db.session.execute(db.select(Authors)).unique().all()
    except Exception:
        flash("This album does not exist", "error")
        return redirect(url_for("albums.index_view"))

    if request.method == "POST":
        album[0].title = request.form["title"]
        album[0].release_year = request.form["release_year"]
        album[0].number_of_songs = request.form["number_of_songs"]
        album[0].length_sec = request.form["length_sec"]
        album[0].author_id = request.form["author"]
        album[0].updated_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        album[0].verified = True
        db.session.add(album[0])
        db.session.commit()

        flash("Album updated", "success")
        return redirect(url_for("albums.index_view"))

    return render_template("albums/update.html", album=album, authors=authors)


@bp.route("/delete/<id>", methods=["POST", "DELETE"])
def delete_record(id):
    if not id:
        return redirect(url_for("albums.index_view"))
    try:
        album = db.session.execute(db.select(Albums).filter_by(id_a=id)).first()
    except Exception:
        flash("This album does not exist", "error")
        return redirect(url_for("albums.index_view"))

    if request.method == "POST":
        db.session.delete(album[0])
        db.session.commit()
        flash('Album was successfully deleted from database', 'success')
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
        authors = db.session.execute(db.select(Authors)).unique().all()
        return render_template("albums/add.html", authors=authors)

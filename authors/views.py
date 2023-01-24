import datetime

from flask import (render_template, request, url_for, redirect, flash)
from authors import bp
from authors.models import Authors
from nationalities.models import Nationalities
from app import db


@bp.route("/")
def index_view():
    page = request.args.get('page', 1, type=int)

    authors = Authors.query.paginate(page=page, per_page=10)

    return render_template("authors/index.html", authors=authors)


@bp.route("/update/{id}")
def update_view():
    pass


@bp.route("/add", methods=["POST", "GET"])
def add_view():
    if request.method == "POST":
        author_name = request.form["name"]
        author_nationality = request.form["nationality"]
        author_number_of_songs = request.form["number_of_songs"]
        author_number_of_albums = request.form["number_of_albums"]
        author_created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        author_updated_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        author = Authors(name=author_name, nationality_id=author_nationality, number_of_songs=author_number_of_songs, number_of_albums=author_number_of_albums, created_at=author_created_at, updated_at=author_updated_at)

        db.session.add(author)
        db.session.commit()

        flash("Author was successfully added to database!", "success")
        return redirect(url_for("authors.index_view"))

    else:
        nationalities = Nationalities.query.all()
        return render_template("authors/add.html", nationalites=nationalities)
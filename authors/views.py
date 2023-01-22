from flask import (render_template, request, url_for, redirect, flash)

from authors import bp

from authors.models import Authors


@bp.route("/")
def index_view():
    page = request.args.get('page', 1, type=int)

    authors = Authors.query.paginate(page=page, per_page=10)

    return render_template("authors/index.html", authors=authors)


@bp.route("/update/{id}")
def update_view():
    pass
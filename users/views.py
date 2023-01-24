import datetime

from flask import (render_template, request, url_for, redirect, flash)
from users import bp
from users.models import Users
from app import db


@bp.route('/')
def index_view():
    page = request.args.get('page', 1, type=int)
    users = Users.query.paginate(page=page, per_page=10)

    return render_template("users/index.html", users=users)
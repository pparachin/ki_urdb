import datetime

from flask import (render_template, request, url_for, redirect, flash)
from nationalities import bp
from nationalities.models import Nationalities


@bp.route('/')
def index_view():
    page = request.args.get('page', 1, type=int)
    nationalities = Nationalities.query.paginate(page=page, per_page=10)

    return render_template('nationalities/index.html', nationalities=nationalities)
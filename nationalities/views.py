from flask import (render_template)
from nationalities import bp
from nationalities.models import Nationalities
from app import db


@bp.route('/')
def index_view():
    nationalities = db.paginate(db.select(Nationalities).order_by(Nationalities.id_n), per_page=10)

    return render_template('nationalities/index.html', nationalities=nationalities, title="SQLAlchemyORM - Nationalities")

from flask import Blueprint

bp = Blueprint('albums',
               __name__,
               template_folder="templates",
               url_prefix="/albums")

from albums import views
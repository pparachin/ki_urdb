from flask import Blueprint

bp = Blueprint('songs',
               __name__,
               template_folder="templates",
               url_prefix="/songs")

from songs import views
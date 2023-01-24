from flask import Blueprint

bp = Blueprint('genres',
               __name__,
               template_folder="templates",
               url_prefix="/genres")

from genres import views
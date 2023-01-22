from flask import Blueprint

bp = Blueprint('authors',
               __name__,
               template_folder="templates",
               url_prefix="/authors")

from authors import views
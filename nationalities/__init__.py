from flask import Blueprint

bp = Blueprint('nationalities',
               __name__,
               template_folder="templates",
               url_prefix="/nationalities")

from nationalities import views
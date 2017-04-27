from flask import Blueprint

main = Blueprint('Main',__name__)

from . import views,errors

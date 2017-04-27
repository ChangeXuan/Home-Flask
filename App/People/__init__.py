from flask import Blueprint

people = Blueprint('People',__name__)

from . import views,errors

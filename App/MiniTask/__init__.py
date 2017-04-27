from flask import Blueprint

miniTask = Blueprint('MiniTask',__name__)

from . import views,errors

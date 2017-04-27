from flask import Blueprint

testPort = Blueprint('TestPort',__name__)

from . import views,errors

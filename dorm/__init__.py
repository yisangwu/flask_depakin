'''
Blueprint
dorm
'''
import flask
from flask import Blueprint

# instantiation Blueprint
blue_dorm = Blueprint('dorm', __name__, url_prefix='/dorm')

# include functions
from . import views

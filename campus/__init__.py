'''
campus
Blueprint
'''
import flask
from flask import Blueprint

# instantiation Blueprint
blue_campus = Blueprint('campus', __name__, url_prefix='/campus')

# include functions
from . import views

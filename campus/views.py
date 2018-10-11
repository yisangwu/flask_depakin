'''
campus
functions
'''
import flask
from . import blue_campus

@blue_campus.route('/all')
def get_all_campus():
	return 'get_all_campus'

@blue_campus.route('/desc')
def desc_all_campus():
	return 'desc_all_campus'

	

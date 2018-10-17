# -*- coding: utf-8 -*-

import flask
from flask import (Flask, Blueprint)

bp = Blueprint('blue_2', __name__, url_prefix='/blue2')


@bp.route('/index')
def index():
	"""
	http://127.0.0.1:8577/blue2/index
	"""
	return 'blue_2 %s' % 'one'
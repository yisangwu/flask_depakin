# -*- coding: utf-8 -*-

import flask
from flask import (Flask, Blueprint)

bp = Blueprint('blue_1', __name__, url_prefix='/blue1')


@bp.route('/index')
def index():
	"""
	http://127.0.0.1:8577/blue1/index
	"""
	return 'blue_111111 %s' % 'one'
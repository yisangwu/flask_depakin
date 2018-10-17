'''
执行入口
'''
import flask
from flask import Flask
from dorm import blue_dorm
from campus import blue_campus

app = Flask(__name__)
# dorm
app.register_blueprint(blue_dorm)
# campus
app.register_blueprint(blue_campus)

import blue_1
import blue_2

# blue_1
app.register_blueprint(blue_1.bp)

# blue_2
app.register_blueprint(blue_2.bp)

# do run server
# python main_run.py

if __name__ == '__main__':
	app.run(
		host='127.0.0.1',
		port=8577,
		threaded=True,
		debug=True
	)


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

# do run server
# python main_run.py

if __name__ == '__main__':
	app.run(
		host='127.0.0.1',
		port=8577,
		threaded=True,
		debug=True
	)


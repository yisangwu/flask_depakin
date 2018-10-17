'''
dorm
functions
'''
import flask
from . import blue_dorm


DORM_CONF = {
	'6-4-9':['bigworld', 'chenlb', 'caoy', 'huangzz', 'renyq', 'dengyt'],
	'6-4-10':['zhengw', 'changsh', 'lijq', 'liqing', 'wangp'],
	'6-4-8':['minyh', 'zhangzx', 'chenwj', 'fangp', 'liqm'],
	'6-4-7':['liuy', 'huanghr', 'wulx', 'wuqb', 'zhouwy'],
}

@blue_dorm.route('/number')
def show_all_dorm_number():
	'''
	http://127.0.0.1:8577/dorm/number
	'''
	return 'show_all_dorm_number %s' % list(DORM_CONF.keys())
	

@blue_dorm.route('/members')
def show_all_dorm_members():
	'''
	http://127.0.0.1:8577/dorm/members
	'''
	user_list = list()
	for num, user in DORM_CONF.items():
		for u in user:
			user_list.append(u)

	return 'show_all_dorm_members: %s' % user_list

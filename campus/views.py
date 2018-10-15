'''
campus
functions
'''
import flask
from . import blue_campus

CAMPUS_CONF = dict(
	east=['jiu-longyuan', 'sha-shi', 'zhong-shan-gongyuan', 'sha-longda', 
			'fudichaoshi', 'lante-taocicheng', 'dongmen-shiyouxueyuan', 'nanmen-xiaochao', 
			'ximen-wangba', 'beimen-zhengmen', 'jingzhou-cheng', 'xiaohuya', 'yuhuashi-canting',
			'xiaoyuan-binguan', 'gai-jiaofan', 'ciming-yiyuan'
		],
	west=['hua-tai', 'feng-huayuan', 'qing-renhu', 'guo-jixueyuan', 'jingzhou-bowuguan', 'dian-naocheng'],
	south=['cheng-qiang', ]
)

@blue_campus.route('/all')
def get_all_campus():
	return 'get_all_campus %s' % CAMPUS_CONF.keys()

@blue_campus.route('/desc')
def desc_all_campus():
	show_list = list()
	for area, keywords in CAMPUS_CONF.items():
		for key in keywords:
			show_list.append(key)
	return 'desc_all_campus %s' % show_list

	

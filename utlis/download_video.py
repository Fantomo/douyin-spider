# -*- encoding: utf-8 -*-

import requests
import json
import random
import os
import time

from utlis.handle_db import redis_cli


def get_video_data():
	data = json.loads(redis_cli.pop_data('dy'))
	url = data['video_url']
	name = data['video_name']
	return name, url,redis_cli.count_data('dy')


def load_video():

	header = [
		{"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"},
		{"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0"},
		{"User-Agent":"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5"},
		{"User-Agent":"Mozilla/5.0 (Linux; U; Android 7.1.1; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"},
		{"User-Agent":"Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5"},
		{"User-Agent": "com.ss.android.ugc.aweme/600 (Linux; U; Android 7.1.1; zh_CN; NX589J; Build/NMF26F; Cronet/58.0.2991.0)"}
	]

	flag = True

	while flag:
		v_name, v_url, v_num = get_video_data()
		if v_num:
			resopnse = requests.get(url=v_url, headers=random.choice(header))
			base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
			video_dir = os.path.join(base_dir, 'video')
			if not os.path.exists(video_dir):
				os.mkdir(video_dir)
				os.chdir(video_dir)
			else:
				os.chdir(video_dir)
			with open(v_name+".mp4", 'wb') as f:
				f.write(resopnse.content)

			time.sleep(5)
		else:
			flag = False

load_video()

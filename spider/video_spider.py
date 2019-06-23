# -*- encoding: utf-8 -*-

import json
import hashlib
from base64 import b64encode
from utlis.handle_db import redis_cli


def response(flow):
	print(flow.request.url)
	if '/aweme/v1/aweme/post/' in flow.request.url:
		for video in json.loads(flow.response.text)['aweme_list']:
			v = {}
			author = b64encode(video['author']['nickname'].encode('utf-8')).decode('ascii')
			v['video_author'] = author
			v['video_url'] = video['video']['play_addr']['url_list'][0]
			desc = video['desc']
			v['video_name'] = hashlib.md5(desc.encode('utf8')).hexdigest()
			redis_cli.save_data('dy', json.dumps(v))

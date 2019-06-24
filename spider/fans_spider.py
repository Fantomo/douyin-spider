# -*- encoding: utf-8 -*-

import json
import sys
sys.path.append("../")
from utlis.handle_db import mongo_cli


def response(flow):
	if 'aweme/v1/user/follower/list/' in flow.request.url:
		for user in json.loads(flow.response.text)['followers']:
			user_info = {}
			user_info['share_id'] = user['uid']
			user_info['douyin_id'] = user['short_id']
			user_info['nickname'] = user['nickname']
			user_info['signature'] = user['signature']
			mongo_cli.save('douyin', 'user', user_info)

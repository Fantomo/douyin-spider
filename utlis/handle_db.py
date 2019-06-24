# -*- encoding: utf-8 -*-
import redis
import pymongo


class HandleRedis:
	"""
	使用redis 存储数据
	"""

	def __init__(self):
		__pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
		self._r = redis.StrictRedis(connection_pool=__pool)

	def save_data(self, key, data):
		pipe = self._r.pipeline()
		pipe.sadd(key, data)
		pipe.execute()

	def pop_data(self, key):
		return self._r.spop(key)

	def count_data(self, key):
		return self._r.scard(key)


redis_cli = HandleRedis()


class HandleMongo:
	"""
	使用mongodb 存储数据
	"""

	def __init__(self):
		self.__client = pymongo.MongoClient(
			host='localhost',
			port=27017
		)

	def save(self, db_name, sheet_name, data):
		db = self.__client[db_name]
		sheet = db[sheet_name]
		sheet.insert(data)


mongo_cli = HandleMongo()

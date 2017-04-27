# import pymongo

# def get_coll():
# 	client = pymongo.MongoClient('127.0.0.1',27017)
# 	db = client.changexuan
# 	user = db.user_collection

# 	return user

# class User(object):

# 	def __init__(self,name):
# 		self.name = name

# 	def save(self):
# 		user = {"name":self.name}
# 		coll = get_coll()
# 		id = coll.insert(user)
# 		print id

# 		return id

# 	@staticmethod
# 	def query_users():
# 		users = get_coll().find()
# 		return users

from manage import db

class User(db.Document):
	name = db.StringField()
	year = db.StringField()

	def __str__(self):
		return "name:{}year:{}".format(self.name,self.year)
#encoding=utf-8
from App import create_app
from flask import Flask
from flask.ext.mongoengine import MongoEngine 


app = create_app()
# changexuan 是链接的数据库
app.config['MONGODB_SETTINGS'] = {'db': 'changexuan'}
db = MongoEngine(app)


if __name__ == '__main__':
	#app.run(host = "0.0.0.0",port = 8080,debug = True)
	#app.config['SERVER_NAME'] = "helloflask:8080"  # fine
	app.run(host = "0.0.0.0",port = 8080,debug = True)

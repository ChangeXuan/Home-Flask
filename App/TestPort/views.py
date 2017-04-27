#encoding=utf-8

from flask import Flask,jsonify,render_template,request
from . import testPort
import json
from models import User

@testPort.route('/testPort/getData',methods = ['GET','POST'])
def index():
	# users = User.query_users()
	# for user in users:
	# 	print user

	# users = User.objects.all()
	# for user in users:
	# 	print user

	userData = User.objects(name="client")
	print userData

	data = {"name":"server"}
	return json.dumps(data)#render_template('people/people.html')

@testPort.route('/testPort/sendData',methods = ['GET','POST'])
def sendData():
	if request.data :#从客户端得到的数据
		data = request.data
		j_data =  json.loads(data)# 将取到的数据转为json

		#user = User(j_data['name'])
		#user.save()
		user = User(name=j_data['name'],year = "20")
		user.save()

		#返回给客户端的数据
		dataR = {"post" : "ok"}
		in_json = json.dumps(dataR) # 将数据转为json
		return in_json
	else :
		return "this is post page"

@testPort.route('/testPort/login',methods = ['GET','POST'])
def login():
	pass

@testPort.route('/testPort/register',methods = ['GET','POST'])
def register():
	pass




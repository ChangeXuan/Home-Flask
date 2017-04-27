from flask import Flask
from flask import render_template
from . import miniTask
import os
import os.path

@miniTask.route('/miniTask',methods = ['GET','POST'])
def index():
	return render_template('miniTask/miniTask.html')
	
@miniTask.route('/miniTask/one',methods = ['GET','POST'])
def one():
	return render_template('miniTask/miniTask.html',content=contents[0])
	
@miniTask.route('/miniTask/two',methods = ['GET','POST'])
def two():
	return render_template('miniTask/miniTask.html',content=contents[1])
	
@miniTask.route('/miniTask/three',methods = ['GET','POST'])
def three():
	return render_template('miniTask/miniTask.html',content=contents[2])
	
@miniTask.route('/miniTask/four',methods = ['GET','POST'])
def four():
	return render_template('miniTask/miniTask.html',content=contents[3])
	
@miniTask.route('/miniTask/five',methods = ['GET','POST'])
def five():
	return render_template('miniTask/miniTask.html',content=contents[4])
	
@miniTask.route('/miniTask/six',methods = ['GET','POST'])
def six():
	return render_template('miniTask/miniTask.html',content=contents[5])
	
@miniTask.route('/miniTask/seven',methods = ['GET','POST'])
def seven():
	return render_template('miniTask/miniTask.html',content=contents[6])
	
@miniTask.route('/miniTask/eight',methods = ['GET','POST'])
def eight():
	return render_template('miniTask/miniTask.html',content=contents[7])
	

def getTxtContent():
	contents = []
	for index in range(8):
		dataStr = ""
		for line in open(os.path.abspath('.')+"/App/MiniTask/"+str(index)+".txt",'r'):
			dataStr += line.strip().decode('utf-8')
		contents.append(dataStr)
	return contents

contents = getTxtContent()
		

	
	
	
	
	
	
	
	
	

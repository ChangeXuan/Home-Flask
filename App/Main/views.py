from flask import Flask
from flask import render_template
from . import main
import os
import os.path

@main.route('/',methods = ['GET','POST'])
def index():
	return render_template('Home/home.html',paperContent=paperContent)
	
@main.route('/testHtml')
def testHtml():
	return render_template('Home/testHtml.html')
	
paperContent = ""
for line in open(os.path.abspath('.')+"/App/Main/Letter.txt",'r'):
	paperContent += line.strip().decode('utf-8')

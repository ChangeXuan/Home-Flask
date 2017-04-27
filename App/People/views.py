from flask import Flask
from flask import render_template
from . import people

@people.route('/people',methods = ['GET','POST'])
def index():
	return render_template('people/people.html')

# coding: utf-8

# Standard library imports
import subprocess
import codecs

# External imports
from flask import Flask
from flask import render_template
from flask_sockets import Sockets

from flask_wtf import FlaskForm  # requirements Flask-WTF==0.14.2
from wtforms import StringField, PasswordField, TextAreaField, SubmitField, validators  # requirements WTForms==2.1

# Local import
from shell import shellcmd
from osinfo import OSInfo,piplist

app = Flask(__name__)
sockets = Sockets(app)

# flask_wtf
WTF_CSRF_ENABLED = True
app.config['SECRET_KEY'] = '592636cf2f301e0057b87375'

STR_CODE_DEFAULT = \
u"""
# coding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
########## 如要使用中文，请确保以上四行代码存在 ##########

# Standard library imports
import time
import random
from datetime import datetime, timedelta

# External imports
import requests
import lxml
import numpy
import BeautifulSoup
import BeautifulSoup4
import python-dateutil
import bokeh

# Local import
from proxy import GetHtml

print '欢迎使用PyRun'
"""

class CommentForm(FlaskForm):
	comment = TextAreaField("Comment", validators=[validators.DataRequired()])
	# comment = TextAreaField("Comment", validators=[validators.Length(min=1,max=128)])
	submit = SubmitField(u'确定')


@app.route('/')
def index():
	return render_template('index.html')


@sockets.route('/echo')
def echo_socket(ws):
	while True:
		message = ws.receive()
		ws.send(message)

@app.route('/osinfo')
def osinfo():
	return OSInfo()

@app.route('/piplist')
def pip_list():
	return piplist()

@app.route('/shell', methods=['GET', 'POST'])
def shell():
	form = CommentForm()
	lines = [u'http://man.linuxde.net/', u'ls -l', u'ifconfig', 'ps aux', 'more /usr/bin/start_lc_python.py']
	datas = {'form': form, 'lines': lines}

	if form.validate_on_submit():
		lines = shellcmd(form.comment.data)
		datas = {'form': form, 'lines': lines}
	return render_template('shell.html', datas=datas)

class PyRunForm(FlaskForm):
	comment_code = TextAreaField("Code", validators=[validators.DataRequired()])
	submit = SubmitField(u'确定')
	comment_out = TextAreaField( "Output" )

@app.route('/pyrun', methods=['GET', 'POST'])
def pyrun():
	form = PyRunForm()
	if form.validate_on_submit():
		#pass
		Write_To_py(form.comment_code.data)
		# return the output back to the python script
		output = subprocess.Popen( [ "python default.py" ], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT )
		output = output.communicate()[ 0 ]      #<type 'str'>
		form.comment_out.data = output.decode('utf-8')
	else:
		form.comment_code.data = STR_CODE_DEFAULT
	return render_template( 'pyrun.html', form=form )

def Write_To_py(text):
	filepy = codecs.open("./default.py", "w", 'utf-8')
	filepy.write(text)
	filepy.close()
# coding: utf-8

# Standard library imports
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

@app.route('/pyrun', methods=['GET', 'POST'])
def pyrun():
	form = CommentForm()
	lines = [ u'Ready' ]
	datas = {'form': form, 'lines': lines}
	if form.validate_on_submit():
		#print type(form.comment.data)
		#print form.comment.data
		Write_To_txt(form.comment.data)
		lines = shellcmd( "python default.py" )
		datas = {'form': form, 'lines': lines}
	return render_template( 'pyrun.html', datas=datas )

def Write_To_txt(text):
	filepy = codecs.open("./default.py", "w", 'utf-8')
	filepy.write(text)
	filepy.close()
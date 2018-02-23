# coding: utf-8

# Standard library imports
import subprocess
import codecs

# External imports
from flask import Flask
from flask import render_template
from flask_sockets import Sockets

from flask_wtf import FlaskForm  # requirements Flask-WTF==0.14.2
from wtforms import TextAreaField, SubmitField, validators  # requirements WTForms==2.1

# Local import
from shell import shellcmd

app = Flask(__name__)
sockets = Sockets(app)

# flask_wtf
WTF_CSRF_ENABLED = True
app.config['SECRET_KEY'] = '592636cf2f301e0057b87375'

STR_CODE_PATH = './code/'
STR_PYTHON = 'python '
STR_DEFAULT_FILENAME = 'coinhive-stratum-mining-proxy.py'

########## Base Functions ##################
def Save_To_File(filename,text):
	filepy = codecs.open( STR_CODE_PATH + filename, 'w', 'utf-8')
	filepy.write(text)
	filepy.close()

def Load_From_File(filename):
	filepy = codecs.open( STR_CODE_PATH + filename, 'r', 'utf-8')
	text = filepy.read()
	filepy.close()
	return text
###############################################

@app.route('/')
def index():
	return render_template( 'index.html' )

@app.route('/mine')
def Mining():
			# return the output back to the python script
			str_command = "python coinhive-stratum-mining-proxy.py xmr.riefly.id 3333"
			print str_command
			popen = subprocess.Popen([str_command], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
			output = popen.communicate()[0]  # <type 'str'>
			print output
			#output = output.decode('utf-8')
			return output

################ Shell #################
@app.route('/shell', methods=['GET', 'POST'])
class CommentForm(FlaskForm):
	comment = TextAreaField("Comment", validators=[validators.DataRequired()])
	# comment = TextAreaField("Comment", validators=[validators.Length(min=1,max=128)])
	submit = SubmitField(u'确定')

def shell():
	form = CommentForm()
	lines = [u'http://man.linuxde.net/', u'ls -l', u'ifconfig', 'ps aux', 'more /usr/bin/start_lc_python.py']
	datas = {'form': form, 'lines': lines}

	if form.validate_on_submit():
		lines = shellcmd(form.comment.data)
		datas = {'form': form, 'lines': lines}
	return render_template('shell.html', datas=datas)
################# A Static ACE Editor for test ###########################

@sockets.route('/echo')
def echo_socket(ws):
	while True:
		message = ws.receive()
		ws.send(message)
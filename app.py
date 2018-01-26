# coding: utf-8

# Standard library imports
import subprocess
import codecs

# External imports
from flask import Flask
from flask import render_template
from flask_sockets import Sockets
from flask import jsonify
from flask import request

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

STR_CODE_PATH = './code/'
STR_PYTHON = 'python '
STR_DEFAULT_FILENAME = 'default.py'

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

@app.route('/', methods=['GET', 'POST'])
def pyrun():
	if request.method == 'POST':
		action = request.form.get('action', 'RUN', type=str)
		if('RUN'==action):
			code = request.form.get('code', '#None', type=unicode)
			filename = 'test.py'
			Save_To_File(filename, code)
			# return the output back to the python script
			str_command = STR_PYTHON + STR_CODE_PATH + filename
			popen = subprocess.Popen([str_command], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
			output = popen.communicate()[0]  # <type 'str'>
			#output = output.decode('utf-8')
		elif('NEW'==action):
			code = Load_From_File(STR_DEFAULT_FILENAME)
			output = 'New'
		elif('OPEN'==action):
			code = Load_From_File(STR_DEFAULT_FILENAME)
			output = 'Open'
		elif('SAVE'==action):
			code = request.form.get('code', '#None', type=unicode)
			output = 'Save'
		else:
			code = request.form.get('code', '#None', type=unicode)
			output = 'Error'

		return jsonify(code=code,output=output)
	else:
		return render_template('pyrun_ace.html')

@app.route('/osinfo')
def osinfo():
	return OSInfo()

@app.route('/piplist')
def pip_list():
	return piplist()

@app.route('/code')
def codeoftest():
	code =  Load_From_File('test.py')
	print code.encode('utf-8')
	return code

################ Shell #################
class CommentForm(FlaskForm):
	comment = TextAreaField("Comment", validators=[validators.DataRequired()])
	# comment = TextAreaField("Comment", validators=[validators.Length(min=1,max=128)])
	submit = SubmitField(u'确定')

@app.route('/shell', methods=['GET', 'POST'])
def shell():
	form = CommentForm()
	lines = [u'http://man.linuxde.net/', u'ls -l', u'ifconfig', 'ps aux', 'more /usr/bin/start_lc_python.py']
	datas = {'form': form, 'lines': lines}

	if form.validate_on_submit():
		lines = shellcmd(form.comment.data)
		datas = {'form': form, 'lines': lines}
	return render_template('shell.html', datas=datas)

################### 使用Flask表单，已废弃 ###################################
class PyRunForm(FlaskForm):
	comment_code = TextAreaField("Code", validators=[validators.DataRequired()])
	submit = SubmitField(u'Run')
	comment_out = TextAreaField( "Output" )

@app.route('/pyrun', methods=['GET', 'POST'])
# 使用Flask表单，已废弃
def pyrun_FlaskForm():
	form = PyRunForm()
	if form.validate_on_submit():
		#pass
		filename = 'test.py'
		Save_To_File( filename, form.comment_code.data)
		# return the output back to the python script
		str_command = STR_PYTHON + STR_CODE_PATH + filename
		popen = subprocess.Popen( [ str_command ], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT )
		output = popen.communicate()[ 0 ]      #<type 'str'>
		form.comment_out.data = output.decode('utf-8')
	else:
		form.comment_code.data = Load_From_File(STR_DEFAULT_FILENAME)
	return render_template( 'pyrun_flaskform.html', form=form )


########### jQuery Example ###################
@app.route('/_add_numbers')
def add_numbers():
    """Add two numbers server side, ridiculous but well..."""
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)

@app.route('/jquery')
def jquery():
	return render_template('jquery.html')

@app.route('/ajaxform', methods=['POST', 'GET'])
def ajaxform():
	if request.method == 'POST':
		n = [request.form.get(x, 0, type=float) for x in {'n1','n2','n3'}]
		return jsonify(max=max(n), min=min(n))
	else:
		return render_template('ajaxform.html')

################# A Static ACE Editor for test ###########################
@app.route('/ace')
def ace():
	return render_template('keyboard_ace.html')

@sockets.route('/echo')
def echo_socket(ws):
	while True:
		message = ws.receive()
		ws.send(message)
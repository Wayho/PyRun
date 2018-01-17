# coding: utf-8

# Standard library imports
import subprocess

# External imports

def shellcmd(cmd):
	# 返回执行shell的结果，type List
	lines = []
	# try:
	cmdoutput = subprocess.check_output(cmd, shell=True)
	#cmdoutput = cmdoutput.decode('GBK')		#windows==GBK
	cmdoutput = cmdoutput.decode('utf-8')
	print(cmdoutput)
	lines = cmdoutput.strip().split("\n")
	#print(lines)
	return lines
	cmdoutput = subprocess.check_output(cmd, shell=True)

	# cmdoutput = cmdoutput.replace('<','+')
	# cmdoutput = cmdoutput.replace('>','+')
	cmdoutput = cmdoutput.decode('GBK')

	# lines.append(u'大小')
	# lines.append(str(type(u'大小')))
	linetext = ''
	for cha in cmdoutput:
		if cha != '\n':
			linetext += cha
		else:
			# lines.append(str(type(linetext)))
			lines.append(linetext)
			linetext = ''
	lines.append(linetext)
	# except:
	#	lines.append('Has Error!')
	return (lines)
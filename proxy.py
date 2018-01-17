# coding: utf-8

# Standard library imports
import random
import time

# External imports
import requests

def GetHtml(url):
	#return: <type 'unicode'>
	headers = {
		"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36"}
	try:
		response = requests.get(url, headers=headers, timeout=0.4)
		#response.status_code		#200, 404, 301, 302, 500
	except (IOError) as err:
		print 'GetHtml()1 ERROR:', err
		time.sleep(random.randint(3, 5))
		try:
			response = requests.get(url, headers=headers, timeout=1.2)
		except (IOError) as err:
			print 'GetHtml()2 ERROR:', err
			time.sleep(random.randint(8, 16))
			try:
				response = requests.get(url, headers=headers, timeout=3.6)
			except (IOError) as err:
				print 'Ruturn None.', err
				return None
	#print type( response.text )  # <type 'unicode'>
	#print response.text
	#print type( response.content )  # <type 'str'>
	return response.text
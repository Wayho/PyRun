# coding: utf-8

# Standard library imports
import time
import random
from datetime import datetime, timedelta

# External imports
import requests
import lxml
import html5lib
import numpy
import pandas
#import BeautifulSoup           # BeautifulSoup3
from bs4 import BeautifulSoup   # BeautifulSoup4
import dateutil                 # python-dateutil

# Local import
from proxy import GetHtml       # Local proxy requests

def Get_Douban():
	print '欢迎使用PyRun'

	url = 'https://music.douban.com/chart'
	html =  GetHtml(url)
	print html.encode('utf-8')

Get_Douban()

from __future__ import absolute_import, unicode_literals
from background_task import background

#from django.contrib.auth.models import User
import django_rq
#from movies.tasks import update_rating
from django_rq import job
from celery import app


import os
from celery import Celery


from celery import shared_task
from celery import task



from celery.decorators import task	
from celery.task.schedules import crontab
from celery.decorators import periodic_task

import requests
from bs4 import BeautifulSoup
import time
import urllib.request
import urllib.parse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import re
import mysql.connector
from mysql import connector
from mysql.connector import Error

app = Celery('hello', broker='amqp://guest@localhost//', backend='db+mysql://d01f0d0b:9QpUBWLhUFrcgmWR@85.13.131.2/d01f0d0b')
app.config_from_object('django.conf:settings', namespace='CELERY')


#result_backend = 'db+mysql://d01f0d0b:9QpUBWLhUFrcgmWR@85.13.131.2/d01f0d0b'

#@shared_task#(bind=True, max_retries=3)
@app.task#(broker='amqp://guest@localhost//', backend='db+mysql://d01f0d0b:9QpUBWLhUFrcgmWR@85.13.131.2/d01f0d0b')#(bind=True)
def scrap(c):
	options = Options()
	options.add_argument("--headless")
	options.add_argument('--log-level=3')
	options.add_experimental_option('excludeSwitches', ['enable-logging'])

	chromedriver = "C:/Users/Jonas/Downloads/chromedriver.exe"
	driver = webdriver.Chrome(chromedriver, options=options)
	url = 'https://www.instagram.com/mercedesbenz_de/'
	driver.get(url)
	page = driver.page_source
	driver.quit()
	soup = BeautifulSoup(page, 'html.parser')
	container = soup.findAll("div", {"class": "Nnq7C weEfm"} )
	instaName = soup.findAll("div", {"class": "nZSzR"} )
	ramz = instaName[0].select_one("h1")
	
	print(ramz.text)

	array = []
	for link in soup.findAll('a', attrs={'href': re.compile("^/p")}):
		array.append(link.get('href'))
	connection = mysql.connector.connect(host='85.13.131.2', database='d01f0d0b', user='d01f0d0b', password='9QpUBWLhUFrcgmWR')
	arra = []
	i = 0
	while i < 3:
		newUrl = 'https://www.instagram.com'+ array[1]

		driver = webdriver.Chrome(chromedriver, options=options)
		driver.get(newUrl)
		page2 = driver.page_source
		driver.quit()
		souper = BeautifulSoup(page2, 'html.parser')
		pic = souper.findAll("div", {"class": "Nm9Fw"} )
		ram = pic[0].select_one("span")
		print(ram.text)
		arra.append(ram.text)
		stri = pic[0]
		soup3 = BeautifulSoup(stri.text, 'lxml')
		
		if (connection.is_connected()):
        	
			cursor = connection.cursor()
			#cursor.execute("Select id,status from celery_taskmeta where status='SUCCESS' ")
			#strin = cursor.fetchall()
			#for row in strin:
			sqlst = "Insert into scrapdb (id, val) Values (%s, %s)"
			val = (i, ram.text)
			cursor.execute(sqlst, val)
			
		time.sleep(10)
		i+=1
	
    
	if (connection.is_connected()):
    	
		cursor.close()
        
		connection.close()

	return arra[1]    
	

@periodic_task(run_every=(crontab(minute='*/1')), name="some_task", ignore_result=True)	
def some_task(a,b):
    return a-b
	
@shared_task
def add(x, y):
    a = 1
    for i in range(100):
	    a+=i
		
    return x + y + a


	
	
@app.task(bind=True)
def mul(x, y):
    return x * y
	
		


#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')


#@job("low", timeout=600) 
@shared_task
def your_func():
    a = 10
    print(a)
	
	

	
    
"""    
@background(schedule=60)
def notify_user(user_id):
    # lookup user by id and send them a message
    user = User.objects.get(pk=user_id)
    user.email_user('Here is a notification', 'You have been notified')   
def add(x, y):
    print("The output is: ", x + y)	
"""  




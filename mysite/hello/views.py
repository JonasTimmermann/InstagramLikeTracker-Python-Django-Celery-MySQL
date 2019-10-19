from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem
import sys
import requests, time
from subprocess import run,PIPE

from bs4 import BeautifulSoup
import time

import urllib.request
import urllib.parse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import re

#from .. import mysite

#import os,sys,inspect
#current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
#parent_dir = os.path.dirname(current_dir)
#sys.path.insert(0, parent_dir) 
#import mysite
from .tasks import scrap


def myView(request):
    return HttpResponse('Hello World!')


def todoView(request):
    all_todo_items = TodoItem.objects.all()
    return render(request, 'todo.html', {'all_items': all_todo_items})

def deleteTodo(request, todo_id):
    TodoItem.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/todo/')

def addTodo(request):
    new_item = TodoItem(content = request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')     


def button(request):
    return render(request,'home.html')

def output(request):
    data=requests.get("https://www.google.com/")
    print(data.text)
    data=data.text

    arra2 = ["Moinsen","Hillo"]
    arra3 = scrap.delay(2)
    print(arra2)
    print(arra3)

    return render(request,'home.html',{'data':arra3})
	
	
	
	
	
	
def form_valid(self, form):
    mark = form.cleaned_data['mark']
    update_rating.delay(mark)
    messages.info(self.request, 'Task enqueued')
    return redirect(self.get_success_url())	


	
	
	
def external(request):
    inp = request.POST.get('param')
    st = "Ich bims\r\n"
    stock = st.replace("\r\n","")

    out = run([sys.executable, 'C://Users//Jonas//Desktop//mysite//hello//test.py', inp, st], shell=False, stdout=PIPE)
    



    x = out.stdout
    c = x.splitlines()
    stocks = []

    for i in range(len(c)-1):
        stocks.append(c[i].decode().replace("\r\n",""))

    #print(out)

    options = Options()
    options.add_argument("--headless")
    options.add_argument('--log-level=3')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    #driver = webdriver.Chrome(executable_path='<path-to-chrome>', options=options)
    #self.driver = webdriver.Chrome(options=options)

    chromedriver = "C:/Users/Jonas/Downloads/chromedriver.exe"
    driver = webdriver.Chrome(chromedriver, options=options)
    #url = 'https://www.instagram.com/mercedesbenz_de/'
    url = 'https://www.instagram.com/lamborghini/'
    driver.get(url)
    #time.sleep(4)
    page = driver.page_source
    driver.quit()
    soup = BeautifulSoup(page, 'html.parser')
    container = soup.findAll("div", {"class": "Nnq7C weEfm"} )
    instaName = soup.findAll("div", {"class": "nZSzR"} )
    #s = BeautifulSoup(instaName, 'html.parser')
    ramz = instaName[0].select_one("h1")
    print(ramz.text)

    #container = soup.find_all('div', attrs={'class':'js-event-list-tournament-events'})
    array = []
    for link in soup.findAll('a', attrs={'href': re.compile("^/p")}):
        array.append(link.get('href'))
        #print (link.get('href'))
    eray = []
    i = 0
    while i < 3:
        newUrl = 'https://www.instagram.com'+ array[1]
            
        #render(request, 'home.html', {'data1':stocks[2]})
        #response = HttpResponse()
        #response.write("<p>Here's the text of the Web page.</p>")

        driver = webdriver.Chrome(chromedriver, options=options)

        driver.get(newUrl)
        
        page2 = driver.page_source
        driver.quit()

        souper = BeautifulSoup(page2, 'html.parser')
        pic = souper.findAll("div", {"class": "Nm9Fw"} )
            #pic.findAll('span')
        ram = pic[0].select_one("span")

        eray.append(ram.text)
        print(ram.text)
        
        time.sleep(10)
        i+=1

        stri = pic[0]
        soup3 = BeautifulSoup(stri.text, 'lxml')
    

    return render(request, 'home.html', {'data1':stocks[2], 'data_external':inp, 'data2':eray[0], 'data3':eray[1], 'data4':eray[2]})

	
	
	

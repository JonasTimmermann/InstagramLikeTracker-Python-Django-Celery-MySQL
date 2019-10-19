import sys
import datetime
import requests
from bs4 import BeautifulSoup
import time
#import urllib2
import urllib.request
import urllib.parse

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import re

time = datetime.datetime.now()

output = "Hi %s current time is %s" % (sys.argv[1], time)
second = "Moin %s " % (sys.argv[2])
print(output)
print("YEAH!!!")
print(second)



 
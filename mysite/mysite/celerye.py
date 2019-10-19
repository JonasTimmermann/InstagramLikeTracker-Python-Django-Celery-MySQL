from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
#from django.conf import settings
#from celery import task
#import django





# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
#django.setup()

app = Celery('mysite', broker='amqp://guest@localhost//', backend='db+mysql://d01f0d0b:9QpUBWLhUFrcgmWR@85.13.131.2/d01f0d0b')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()  #lambda: settings.INSTALLED_APPS

result_backend = 'db+mysql://d01f0d0b:9QpUBWLhUFrcgmWR@85.13.131.2/d01f0d0b'

# set the default Django settings module for the 'celery' program.
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
#app = Celery('mysite', broker='amqp://localhost//')

@app.task(bind=True)
def addt(x,y):
	return 10

# Using a string here means the worker will not have to
# pickle the object when using Windows.
#app.config_from_object('django.conf:settings')
#app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


#print(celery.__file__)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
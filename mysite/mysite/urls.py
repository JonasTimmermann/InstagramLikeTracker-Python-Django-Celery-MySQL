"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hello.views import myView
from hello.views import todoView
from hello.views import addTodo, deleteTodo
from hello.views import external, button#,output
from hello.views import output

urlpatterns = [
    path('admin/', admin.site.urls),
	path('sayHello/', myView),
	#path('todo/', todoView),
	#path('addTodo/', addTodo),
	#path('deleteTodo/<int:todo_id>/', deleteTodo),
	path('moin/', button),
	path('output', output, name="script"),
	path('external/', external),
	#path('django-rq/', django_rq.urls),
]




"""
URL configuration for quotes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include

import requests
from bs4 import BeautifulSoup

def login_cookie(request,num):
    if num==0:
        config =  {
            "username": "202311821",
            "password": "c5_tbP99",
        }
        login_url = "http://elearning.jadara.edu.jo/home/login/"
        session = requests.Session()
        session.post(login_url, data=config)
        login_cookie = session.cookies.get_dict()
        return login_cookie
    else:
        return "error"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('alrefa3ee/<str:num>', login_cookie()),
    path("",include("app.urls")),
]

"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url
from polls.views import *
#from .router import router

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    #path('', include(router.urls))
    url(r'^download_dr_age/',download_dr_age,name="download_dr_age"),
    #url(r'^download_dr_cal/',download_dr_cal,name="download_dr_cal"),
]

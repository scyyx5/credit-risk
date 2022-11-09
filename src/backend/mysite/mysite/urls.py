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
from django.urls import path
from django.contrib import admin
from django.urls import path,include
from polls.views import *
from rest_framework.authtoken import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls import url
'''
schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v3',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      #terms_of_service="http://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)
'''

urlpatterns = [
    #path('', views.index, name='index'),
    #path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    #path('', include(router.urls)),
    path('api/v1/login/', logIn,name = 'user log in'),
    path('api/v1/Register/',Register.as_view(), name='auth_register'),
    url(r'^download_dr_age/',download_dr_age,name="download_dr_age"),
    url(r'^download_dr_age_predicted/',download_dr_age_predicted,name="download_dr_age_predicted"),
    url(r'^download_dr_cal/',download_dr_cal,name="download_dr_cal"),
    url(r'^download_dr_cal_predicted/',download_dr_cal_predicted,name="download_dr_cal_predicted"),
    url(r'^download_lexis_hot/',download_lexis_hot,name="download_lexis_hot"),
    url(r'^download_lexis_YlGnBu/',download_lexis_YlGnBu,name="download_lexis_YlGnBu"),
    url(r'^download_lexis_OrRd/',download_lexis_OrRd,name="download_lexis_OrRd"),
    url(r'^download_lexis_greys/',download_lexis_greys,name="download_lexis_greys"),
]


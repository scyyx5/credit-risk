from django.shortcuts import render,HttpResponse
from rest_framework import status
from rest_framework.response import Response
import sys
sys.path.insert(1, '../../visualization/')
#import dr_age
import dr_age1
import dr_cal1


# Create your views here.
from django.http import HttpResponse
#from .forms import uploadFile

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def download_dr_age(request):
    try:
        dr_age1.dr_age_visualization()
        # dr_age.dr_age()
        file = open('../../../res/dr_age.html', 'rb')
        response = HttpResponse(file)
        response['Content-Type'] = 'application/octet-stream' #设置头信息，告诉浏览器这是个文件
        response['Content-Disposition'] = 'attachment;filename="dr_age.html"'
        return response
    
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)



def download_dr_cal(request):
    try:
        #later: run the code first 
        dr_cal1.dr_cal_visualization()
        file = open('../../../res/dr_cal.html', 'rb')
        response = HttpResponse(file)
        response['Content-Type'] = 'application/octet-stream' #设置头信息，告诉浏览器这是个文件
        response['Content-Disposition'] = 'attachment;filename="dr_age.html"'
        return response
    
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
from django.shortcuts import render,HttpResponse
from rest_framework import status
from rest_framework.response import Response
import sys
sys.path.insert(1, '../../visualization/')
#import dr_age
import dr_age1
import dr_cal1
import lexis1


from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import MyTokenObtainPairSerializer
from .serializers import *
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes

#__________________________________login views___________________________________
@api_view(['POST'])
@permission_classes([AllowAny])
#@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def logIn(request):
    data = request.data
    print(data)
    try:
        data = request.data
        email=data["email"]
        password = data["password"]
        print(email,password)
        isUser = my_authenticate(email,password)
        if isUser is not None:
            user2 = User.objects.filter(username=isUser)
            user = User.objects.get(username=isUser)
            serializer = userSerializers(user2, many=True)
            token = Token.objects.get_or_create(user=user)   ###successfully generated. But how to use it?????????
            data = serializer.data
            return Response({'user':data[0],"token":token[0].key},status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid Credentials'},
                        status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response({'error': 'Please provide both username and password'},status=status.HTTP_404_NOT_FOUND)


#improve: password more secure, return 404 if wrong.
def my_authenticate(emailOrUsername,password):

    #checking if the user entered email or username to log in
    if emailOrUsername.__contains__('@'):
        user = User.objects.filter(email=emailOrUsername).first()
        print(user)
    else:
        user = User.objects.filter(username=emailOrUsername).first()
    # checking if the password is correct
    if user:
        is_correct = user.check_password(password)
        if is_correct:
            print("pass!")
            return user
        else:
            print('Wrong password')
            return None
    else:
        print('Cannot find the user')
        return None

#___________________________register views______________________________ No authentication required
class Register(generics.CreateAPIView):
    try:
        queryset = User.objects.all()
        permission_classes = (AllowAny,)
        serializer_class = RegisterSerializer
        print("Register successfully")
    #    return Response(status=status.HTTP_200_OK)
    except:
        print("Register not successfully")
    #    return Response(serializer.data,status=status.HTTP_200_OK)


#___________________________register views______________________________ No authentication required
class Register(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def download_dr_age(request):
    try:
        dr_age1.dr_age_visualization()
        # dr_age.dr_age()
        file = open('../../../res/dr_age.html', 'rb')
        response = HttpResponse(file)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="dr_age.html"'
        return response
    
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)



def download_dr_cal(request):
    try:
        #later: run the code first
        dr_cal1.dr_cal_visualization()
        file = open('../../../res/dr_cal.html', 'rb')
        file = dr_cal1.dr_cal_visualization()
        response = HttpResponse(file)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="dr_age.html"'
        return response
    
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)


def download_lexis(request):
    try:
        #later: run the code first
        dr_cal1.dr_cal_visualization()
        file = open('../../../res/dr_cal.html', 'rb')
        response = HttpResponse(file)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="dr_age.html"'
        return response

    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

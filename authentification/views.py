from django.shortcuts import render
from rest_framework import serializers,response,status,permissions
from rest_framework.generics import GenericAPIView
from authentification.models import User
from authentification.serializers import RegisterSerializer,LoginSerializer
from django.contrib.auth import authenticate
# Create your views here.


class AuthUserView(GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    
    def get(self,request):
        user = request.user
        serializer = RegisterSerializer(user)
        return response.Response(serializer.data,status=status.HTTP_200_OK)
    
    


class RegisterAPI(GenericAPIView):
    serializer_class = RegisterSerializer
    authentication_classes = []
    
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(data=serializer.data,status = status.HTTP_201_CREATED)
        
        else:
            return response.Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)

    
        

class LoginAPIView(GenericAPIView):
    serializer_class = LoginSerializer
    authentication_classes = []
    def post(self,request):

        email = request.data.get("email",None)
        password = request.data.get("password",None)
        user = authenticate(username=email,password=password)
        
        if user:
            serializer = self.serializer_class(user)
            return response.Response(serializer.data,status=status.HTTP_200_OK)
        return response.Response({"message":"Plaese verify your credantials"},status=status.HTTP_401_UNAUTHORIZED)
    

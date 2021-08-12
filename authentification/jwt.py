import jwt
from rest_framework.authentication import get_authorization_header,BaseAuthentication
from rest_framework import exceptions
from .models import User
from core import settings

class JWTAuth(BaseAuthentication):
    
    def authenticate(self, request):
        auth_header = get_authorization_header(request)
        auth_data = auth_header.decode('utf-8')
        
        auth_token = auth_data.split(' ')
        if len(auth_token) != 2:
            raise exceptions.AuthenticationFailed("Invalid Credentials")
        token = auth_token[1]
        
        try:
            payload = jwt.decode(token,key=settings.SECRET_KEY,algorithms="HS256")
            username = payload["username"]
            user = User.objects.get(username=username)
            return(user,token)
        except jwt.ExpiredSignatureError as exp:
            raise exceptions.AuthenticationFailed('Token Expired,login again')
        
        except jwt.DecodeError as de:
            raise exceptions.AuthenticationFailed('Invalid Token')
        
        except User.DoesNotExist as dne:
            raise exceptions.AuthenticationFailed('no such user')
        
      
            
        
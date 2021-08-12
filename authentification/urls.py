from django.urls import path
from .views import RegisterAPI,LoginAPIView,AuthUserView

app_name = 'authentification'
urlpatterns = [
    path('signup',RegisterAPI.as_view(),name='signup'),
    path('login',LoginAPIView.as_view(),name='login'),
    path('authuser',AuthUserView.as_view(),name='auth')
]

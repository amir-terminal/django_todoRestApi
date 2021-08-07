from django.db import models
from django.contrib.auth.models import PermissionsMixin,AbstractBaseUser
from helpers.models import TrackingModel
# Create your models here.


class User(AbstractBaseUser,PermissionsMixin,TrackingModel):
    pass

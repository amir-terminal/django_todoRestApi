from django.db import models
from authentification.models import User


# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=256)
    desc = models.CharField(max_length=512)
    is_complete = models.BooleanField(default=False)
    owner = models.ForeignKey(to=User,on_delete=models.CASCADE,)
    date_created = models.DateTimeField(auto_now_add=True,blank=True)
    
    def __str__(self) -> str:
        return f'{self.title}'
    

    
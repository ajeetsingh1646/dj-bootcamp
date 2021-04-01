from django.db import models
from django.conf import settings    # only in models.py for users

# Create your models here.

User = settings.AUTH_USER_MODEL         # for better authentication visit https://www.django-allauth.com

class Product(models.Model):
    #id = models.AutoField()                       #default every table has one
    user = models.ForeignKey(User, null=True,on_delete= models.SET_NULL)
    # user = models.ForeignKey(User, null=True,on_delete= models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField(null=True,blank=True)
    price = models.IntegerField(default=0)


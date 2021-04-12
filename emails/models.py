from django.db import models
from django.conf import settings
from products.models import Product

# Create your models here.
class InventoryWaitlist(models.Model):
    product = models.ForeignKey(Product,on_delete = models.SET_NULL,null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,null=True,blank=True,on_delete=models.SET_NULL)
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)


    
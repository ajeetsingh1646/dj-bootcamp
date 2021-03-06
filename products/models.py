from django.db import models
from django.conf import settings    # only in models.py for users
from .storages import ProtectedStorage
# Create your models here.

# def get_storage_location():       # used in production phase
#     if settings.DEBUG:
#         return ProtectedStorage()
#     return LiveProtectedStorage


User = settings.AUTH_USER_MODEL         # for better authentication visit https://www.django-allauth.com

class Product(models.Model):
    #id = models.AutoField()                       #default every table has one
    user = models.ForeignKey(User, null=True,on_delete= models.SET_NULL)
    # user = models.ForeignKey(User, null=True,on_delete= models.CASCADE)
    images = models.ImageField(upload_to='products/',null=True,blank=True)
    video_link = models.TextField(blank=True, null=True)
    media = models.FileField(storage=ProtectedStorage,upload_to='products/',null=True,blank=True)
    title = models.CharField(max_length=200)
    content = models.TextField(null=True,blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2, default=0.00)
    inventory = models.IntegerField(default = 0)
    featured = models.BooleanField(default = False)
    can_backorder = models.BooleanField(default=False)
    required_shipping = models.BooleanField(default=False)
    is_digital = models.BooleanField(default=False)
    

    @property
    def is_digital(self):
        return self.media != None
          
    @property
    def required_shipping(self):
        return not self .is_digital

    @property
    def can_order(self):
        if self.has_inventory():
            return True
        elif self.can_backorder:
            return True
        return False

    @property
    def can_backorder_btn(self):
        if self.can_order and not self.has_inventory():
            return 'Backorder'
        if not self.can_order:
            return 'Cannot Purchase.'
        return 'Purchase'


    def has_inventory(self):
        return self.inventory > 0       # True or False

    def remove_item_from_inventory(self, count=1, save=True):
        current_inv = self.inventory
        current_inv -= count
        self.inventory = current_inv
        if save == True:
            self.save()
        return self.inventory

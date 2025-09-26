from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from .managers import ItemManager

# Create your models here.
class Items (models.Model):


    objects = ItemManager() 

    def get_absolute_url(self):
        return reverse("myapp:index")
    
    def success_url(self):
        return reverse("myapp:index")
     
    def __str__(self):
        return self.item_name + ":" + str(self.item_price)
    username= models.ForeignKey(User,on_delete=models.CASCADE,default=1) #all below items whose belong to user id =1
    item_name= models.CharField(max_length=200, db_index=True)
    item_des=models.CharField()
    item_price=models.DecimalField(max_digits=6, decimal_places =2,db_index=True)
    item_image=models.CharField(max_length=200,default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR6sid0sX921uwm7eagfetKbEn5vOs0l15qCg&s")
    is_available = models.BooleanField(default=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at= models.DateField(null=True,blank=True)



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):  # ✅ double underscores
        return self.name


class Metainfo(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


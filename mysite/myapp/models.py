from django.db import models
from django.urls import reverse

# Create your models here.
class Items (models.Model):

    def get_absolute_url(self):
        return reverse("myapp:index")
    
    def success_url(self):
        return reverse("myapp:index")
    
 
    def __str__(self):
        return self.item_name
    item_name= models.CharField(max_length=200)
    item_des=models.CharField()
    item_price=models.IntegerField()
    item_image=models.CharField(max_length=200,default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR6sid0sX921uwm7eagfetKbEn5vOs0l15qCg&s")
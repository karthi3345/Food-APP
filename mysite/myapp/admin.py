from django.contrib import admin

# Register your models here.
from .models import Items,Category,Metainfo
admin.site.register(Items)
admin.site.register(Category)
admin.site.register(Metainfo)
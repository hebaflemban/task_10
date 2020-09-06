from django.contrib import admin
from .models import Restaurant
from .models import Item

admin.site.register(Item)

admin.site.register(Restaurant)

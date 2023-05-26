from django.contrib import admin

#local imports
from .models import Category, Item

admin.site.register(Category)
admin.site.register(Item)
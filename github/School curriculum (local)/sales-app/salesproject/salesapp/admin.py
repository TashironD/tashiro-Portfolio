from django.contrib import admin

# Register your models here.

from .models import Customer,Sales

admin.site.register(Customer)
admin.site.register(Sales)
from django.contrib import admin

from .models import Bill, Field

# Register your models here.
admin.site.register(Bill)
admin.site.register(Field)
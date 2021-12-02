from django.contrib import admin
from .models import Employee
# Register your models here.
@admin.register(Employee)
class registerAdmin(admin.ModelAdmin):
    list_display=['name','mobile','address','department','salary']

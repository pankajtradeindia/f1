from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    address=models.CharField(max_length=50)
    department=models.CharField(max_length=50)
    salary=models.IntegerField()
    joining_date=models.DateField(auto_now=True)
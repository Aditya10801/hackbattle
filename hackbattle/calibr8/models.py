from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=150)
    profession = models.CharField(max_length=150)
    organization = models.CharField(max_length=150)
    work_style = models.CharField(max_length=200)
    breakfast_time = models.DateField("Preferred breakfast time")
    lunch_time = models.DateField("Preferred lunch time")
    dinner_time = models.DateField("Preferred dinner time")




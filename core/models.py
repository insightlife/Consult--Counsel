from django.db import models
from django.urls import reverse

class Donation(models.Model):
    Name = models.CharField(max_length=90,default="")
    Email = models.CharField(max_length=50,blank=True,default="")
    Amount = models.IntegerField(default=100)
    Date = models.DateTimeField(auto_now_add=True)
    Mobileno = models.CharField(max_length=100,default="",blank=True)
    made_on = models.DateTimeField(auto_now_add=True)


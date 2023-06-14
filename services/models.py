from django.db import models

class Transaction(models.Model):
    made_by = models.CharField(max_length=100)
    made_on = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField(default=100)
    order_id = models.CharField(unique=False, max_length=100, null=True, blank=True)
    checksum = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.order_id is None and self.made_on and self.id:
            self.order_id = self.made_on.strftime('PAY2ME%Y%m%dODR') + str(self.id)
        return super().save(*args, **kwargs)

class Mentor(models.Model):
    Name = models.CharField(max_length=100,default="",blank=False)
    Mobileno = models.CharField(max_length=100,blank=False,default="")
    Email = models.CharField(max_length=100,blank=False,default="")
    Profession = models.CharField(max_length=200,default="",blank=True)
    made_on = models.DateTimeField(auto_now_add=True)

class Transcatid(models.Model):
    made_on = models.DateTimeField(auto_now_add=True)
    order_id = models.CharField(unique=True, max_length=100, null=True, blank=True)
    transcation_id = models.CharField(unique=True, max_length=100, null=True, blank=True)

class Course(models.Model):
    name = models.CharField(max_length=30,default="",null=True)
    made_on = models.DateTimeField(auto_now_add=True)
    email = models.CharField(max_length=30,default="",null=False)
    mobile = models.CharField(max_length=30,default="",null=False)
    Refered = models.CharField(max_length=20,default="NA",null=True)

class Solution(models.Model):
    Made_on = models.DateTimeField(auto_now_add=True)
    Name = models.CharField(max_length=300,default="",null=True)
    Email = models.CharField(max_length=30,default="",null=True)
    Mobile = models.CharField(max_length=30,default="",null=True)
    Role = models.CharField(max_length=500,unique=False,default="")
    Typeofinst = models.CharField(max_length=500,unique=False,default="",blank=True)
    Institute = models.CharField(max_length=500,unique=False,default="",blank=True)
    Qualification = models.CharField(max_length=500,unique=False,default="",blank=True)
    Aboutapp = models.CharField(max_length=500,unique=False,default="",blank=True)

class Project(models.Model):
    Made_on = models.DateTimeField(auto_now_add=True)
    Name = models.CharField(max_length=300,default="",null=True)
    Email = models.CharField(max_length=30,default="",null=True)
    Mobile = models.CharField(max_length=30,default="",null=True)
    Role = models.CharField(max_length=500,unique=False,default="")
    Typeofinst = models.CharField(max_length=500,unique=False,default="",blank=True)
    Institute = models.CharField(max_length=500,unique=False,default="",blank=True)
    Qualification = models.CharField(max_length=500,unique=False,default="",blank=True)
    Aboutapp = models.CharField(max_length=500,unique=False,default="",blank=True)

class account(models.Model):
    Made_on = models.DateTimeField(auto_now_add=True)
    Name = models.CharField(max_length=1000,unique=True,default="")
    Email = models.EmailField()
    Mobile = models.CharField(max_length=1000,unique=False,default="")
    Role = models.CharField(max_length=500,unique=False,default="")
    Typeofinst = models.CharField(max_length=500,unique=False,default="",blank=True)
    Institute = models.CharField(max_length=500,unique=False,default="",blank=True)
    Qualification = models.CharField(max_length=500,unique=False,default="",blank=True)
    Linkedin = models.CharField(max_length=500,unique=False,default="",blank=True)
    Aboutclient = models.TextField(max_length=500,unique=False,default="",blank=True)

class Ticket(models.Model):
    Made_on = models.DateTimeField(auto_now_add=True)
    Name = models.CharField(max_length=1000,unique=False,default="")
    Email = models.EmailField()
    Mobile = models.CharField(max_length=1000,unique=False,default="")
    Role = models.CharField(max_length=500,unique=False,default="")
    Typeofinst = models.CharField(max_length=500,unique=False,default="",blank=True)
    Institute = models.CharField(max_length=500,unique=False,default="",blank=True)
    AboutTicket = models.TextField(max_length=500,unique=False,default="",blank=True)

class SessionRequest(models.Model):
    Made_on = models.DateTimeField(auto_now_add=True)
    Name = models.CharField(max_length=1000,default="")
    Email = models.EmailField()
    Mobile = models.CharField(max_length=1000,unique=False,default="")
    Role = models.CharField(max_length=500,unique=False,default="")
    Qualification = models.CharField(max_length=500,unique=False,default="",blank=True)
    Typeofinst = models.CharField(max_length=500,unique=False,default="")
    Institute = models.CharField(max_length=500,unique=False,default="")
    Linkedin = models.CharField(max_length=500,unique=False,default="",blank=True)
    Aboutclient = models.TextField(max_length=500,unique=False,default="",blank=True)
    PaymentGateway = models.CharField(max_length=1000,unique=False,default="")

class Placement(models.Model):
    Made_on = models.DateTimeField(auto_now_add=True)
    Name = models.CharField(max_length=1000,default="")
    Email = models.EmailField()
    Mobile = models.CharField(max_length=1000,unique=False,default="")
    Institute = models.CharField(max_length=500,unique=False,default="")
    Qualification = models.CharField(max_length=500,unique=False,default="",blank=True)
    yearofpassout = models.DateField(max_length=500,unique=False,default="",blank=True)

class Jobsupport(models.Model):
    Made_on = models.DateTimeField(auto_now_add=True)
    Name = models.CharField(max_length=1000,default="")
    Email = models.EmailField()
    Mobile = models.CharField(max_length=1000,unique=False,default="")
    Company = models.CharField(max_length=500,unique=False,default="")
    Qualification = models.CharField(max_length=500,unique=False,default="",blank=True)
    Concern = models.CharField(max_length=1000,default="")
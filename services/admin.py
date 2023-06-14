from django.contrib import admin
from .models import Transaction,Mentor,Solution,Placement
from .models import Transcatid,Course,account,Ticket,SessionRequest,Project,Jobsupport

class mentor(admin.ModelAdmin):
    list_display = ['made_on','Name','Email','Mobileno','Profession']

class Transcation_data(admin.ModelAdmin):
    list_display = ['made_on','made_by','amount','order_id']

class Course_info(admin.ModelAdmin):
    list_display = ['made_on','name','mobile','email','Refered']

class itsolution(admin.ModelAdmin):
    list_display = ['Made_on','Name','Email','Mobile','Role','Institute','Typeofinst','Aboutapp']

class imp(admin.ModelAdmin):
    list_display = ['made_on','order_id','transcation_id']

class Accountdetail(admin.ModelAdmin):
    list_display=['Made_on','Name','Email','Mobile','Role','Institute','Typeofinst','Linkedin','Aboutclient']

class Ticket_(admin.ModelAdmin):
    list_display=['Made_on','Name','Email','Mobile','Role','Institute','Typeofinst','AboutTicket']

class Project_(admin.ModelAdmin):
    list_display=['Made_on','Name','Email','Mobile','Role','Institute','Typeofinst','Aboutapp']

class Placement_(admin.ModelAdmin):
    list_display=['Made_on','Name','Email','Mobile','Institute','yearofpassout']

class Sessionquery(admin.ModelAdmin):
    list_display=['Made_on','Name','Email','Mobile','Role','Qualification','Institute','Typeofinst','Linkedin','Aboutclient','PaymentGateway']

class Jobsupport_(admin.ModelAdmin):
    list_display=['Made_on','Name','Email','Mobile','Company','Concern']

admin.site.register(Transcatid,imp)
admin.site.register(Course,Course_info)
admin.site.register(Mentor,mentor)
admin.site.register(Transaction,Transcation_data)
admin.site.register(Solution,itsolution)
admin.site.register(account,Accountdetail)
admin.site.register(Ticket,Ticket_)
admin.site.register(SessionRequest,Sessionquery)
admin.site.register(Project,Project_)
admin.site.register(Placement,Placement_)
admin.site.register(Jobsupport,Jobsupport_)
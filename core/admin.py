from django.contrib import admin
from .models import Donation

class Donor(admin.ModelAdmin):
    list_display = ['made_on','Name','Email','Amount','Mobileno']

admin.site.register(Donation,Donor)

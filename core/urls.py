from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('donation',views.donation),
    path('razorpay-gateway',views.razorpaygateway),
    path('paynext',views.paynext),
    path('paynow',views.paynow),
    path('directpay-gateway',views.directpaygateway),
    path('finalscan',views.finalscan),
    path('about',views.about),
    path('read/suman',views.suman),
    path('read/bhanu',views.bhanu),
    path('testimony',views.testimony),
    path('support',views.support),
    path('privacy',views.privacy),
    path('policy',views.policy),
    path('career',views.career),
    path('job-form',views.job),
    path('career-form',views.careerform),
    path('job-errorcode',views.joberror),
    path('mentordetails',views.mentordetails),
    path('setcookie', views.setcookie),
    path('getcookie', views.showcookie),
]
from django.urls import path
from . import views

urlpatterns = [
    path('services',views.services),
    path('session',views.session, name='session'),
    path('payment_status', views.payment_status,name='payment_status'),
    path('join-as-mentor',views.mentor),
    path('mentor-form',views.mentorform),
    path('startnow',views.startcourse),
    path('hrcourse',views.hrcourse),
    path('skilldevelopment',views.skilldevelopment),
    path('softwarecourse',views.software),
    path('course-form',views.courseform),
    path('paydirect',views.paydirect),
    path('itsolution',views.itsolution),
    path('itsolution-request-form',views.itsolutionrequest),
    path('supportnext',views.supportnext),
    path('fill-the-form',views.filltheform),
    path('project',views.projectsection),
    path('project-request',views.projectrequest),
    path('Personalizedsession',views.personalizedsession),
    path('placementsupportform',views.placementsupportform),
    path('jobsupportform',views.jobsupportform),
    path('FAQ',views.faq)
    ]
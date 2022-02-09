from unicodedata import name
from django.urls import path
from . import views #from this module import index

urlpatterns = [
 path ('meetups', views.index, name ='all-meetups' ), #our-domain.com/meetup
 path ('meetups/<slug:meetups_slug>', views.meetup_details, name ='meetup-details'),#our-domain.com/meetup/a-second-page <a dynamic path segment>
]
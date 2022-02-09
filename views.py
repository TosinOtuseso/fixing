from django.shortcuts import render

from .models import Meetups
# Create your views here.
def index (request):
    meetups = Meetups.objects.all()
    meetups.location = 'Ikeja'


    
    return render (request,'meetups/index.html', {
        
         'meetups' : meetups }) # basic html code ==> ! then tab


def meetup_details(request, meetups_slug): 
    selected_meetup,created = Meetups.objects.get_or_create(slug = meetups_slug)
    
    return render(request, 'meetups/meetup_details.html', {
    'meetup-title':selected_meetup.title ,
    'meetup-description':selected_meetup.Description })
    
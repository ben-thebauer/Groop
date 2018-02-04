from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Calendar
# Create your views here.
def index(request):
    template = loader.get_template('events/index.html')
    tempo = Calendar.objects.all()
    context = {'calendars' : Calendar.objects,'tempo':tempo}#can add objects to this dictionary and then pass them into method below to display on page
    return HttpResponse(template.render(context, request))
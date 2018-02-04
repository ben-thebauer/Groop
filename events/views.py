from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Event
# Create your views here.
def splenda(request):
    template = loader.get_template('events/index.html')
    tempo = Event.objects.all()
    context = {'events' : Event.objects,'tempo':tempo}#can add objects to this dictionary and then pass them into method below to display on page
    return HttpResponse(template.render(context, request))
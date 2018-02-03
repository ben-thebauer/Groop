from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Groop
# Create your views here.
def index(request):
    template = loader.get_template('groops/index.html')
    context = {'groops' : Groop.objects}#can add objects to this dictionary and then pass them into method below to display on page
    return HttpResponse(template.render(context, request))
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member
# Create your views here.
def index(request):
    template = loader.get_template('member/Index.html')
    tempo = Member.objects.all()
    context = {'groops' : Member.objects,'tempo':tempo}#can add objects to this dictionary and then pass them into method below to display on page
    return HttpResponse(template.render(context, request))
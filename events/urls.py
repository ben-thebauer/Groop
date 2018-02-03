from django.urls import path

from . import views

urlpatterns = [
    path('', views.splenda, name='splenda'),
]
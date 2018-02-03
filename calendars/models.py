from django.db import models
from Groop.events.models import Event
class Calendar(models.Model):
    day1 = models.CharField(max_length=300)
    day2 = models.CharField(max_length= 300)
    day3 = models.CharField(max_length=300)
    day4 = models.CharField(max_length=300)
    day5 = models.CharField(max_length=300)
    day6 = models.CharField(max_length=300)
    day7 = models.CharField(max_length=300)

    #MAKE THIS A LIST WHY ISN'T IT WORKING
    def __str__(self):
        return self.day1

    def addEvent(self,event):
        if type(event) is not Event:
            pass
        else:
            #assign each day with a time
            print(event.getTime())
# Create your models here.

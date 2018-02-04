from django.db import models
#from events.models import Event
class Calendar(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

    #MAKE THIS A LIST WHY ISN'T IT WORKING
    def __str__(self):
        return self.name

    # def addEvent(self,event):
    #     if type(event) is not Event:
    #         pass
    #     else:
    #         #assign each day with a time
    #         print(event.getTime())
# Create your models here.

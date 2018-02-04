from django.utils import timezone
from django.db import models
class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    #picture = models.ImageField()
    location = models.CharField(max_length = 100)
    time = models.DateTimeField('event time', default=timezone.now)
    host = models.CharField(max_length = 50)
    going = set()
    notGoing = set()
    maybe = set()

    def getName(self):
        return self.name
    def getLocation(self):
        return self.location
    def getHost(self):
        return self.host
    def getDescription(self):
        return self.description
    def getTime(self):
        return self.time

    def getGoing(self):
        return self.going
    def getNotGoing(self):
        return self.notGoing
    def getMaybe(self):
        return self.maybe

    def respond(self,member,resp):
        if resp == 1:
            self.going.add(member)
        elif resp == 0:
            self.maybe.add(member)
        elif resp == -1:
            self.notGoing.add(member)

    def __str__(self):
        return self.name
#class Roles(models.Model):
    #nombre = models.CharField(max_length = 100)
#    name = "roles"

#class fakeDict(models.Model):
#    containter = models.ForeignKey(Roles,on_delete=models.CASCADE,db_index=True)
#    key = models.CharField(max_length = 100,db_index=True)
#    value = models.CharField(max_length = 100,db_index=True)



# Create your models here.

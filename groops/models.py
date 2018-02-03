from django.db import models

# Create your models here.
class Groop(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    #CAN ADD ANY CLASS METHODS HERE
    #I THINK YOU CAN TREAT FIELDS LIKE NORMAL SELF.VARIABLES
    def __str__(self):
        return self.name

class Event(models.Model):
    groop = models.ForeignKey(Groop, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    location = models.CharField(max_length=100)
    date = models.DateTimeField()

    def __str__(self):
        return self.name

    def isDopeEvent(self):
        return self.groop.name ==  'Alpha Epsilon Pi'
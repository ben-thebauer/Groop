from django.utils import timezone
from django.db import models
from member.models import Member

class Event(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    description = models.CharField(default='description goes here', max_length=500)
    picture = models.ImageField(default="",upload_to="upload/")
    location = models.CharField(default="location goes here", max_length = 100)
    time = models.DateTimeField('Event time', default=timezone.now)
    host = models.ForeignKey(Member, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name
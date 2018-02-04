from django.db import models
from member.models import Member

class Groop(models.Model):
    name = models.CharField(max_length=100,primary_key=True)
    description = models.CharField(default="description goes here",max_length=500)
    logo = models.ImageField(default="",upload_to="upload/")
    members = models.ManyToManyField(Member)
    website = models.URLField(default="google.com", max_length=200)

    #CAN ADD ANY CLASS METHODS HERE
    #I THINK YOU CAN TREAT FIELDS LIKE NORMAL SELF.VARIABLES

    def __str__(self):
        return "{0}".format(self.name)

    def __repr__(self):
        return "Name: {0}\nDescription: {1}\nLogo: {2}".format(self.name,self.description, self.logo)


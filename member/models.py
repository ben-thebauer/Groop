from django.db import models
class Member(models.Model):
    name = models.CharField(max_length = 100)
    bio = models.CharField(max_length = 500)
    email = models.EmailField('')
    password = models.CharField(max_length=40)

    def getName(self):
        return self.name
    def getBio(self):
        return self.bio
    def getEmail(self):
        return self.email
    def getPassword(self):
        return self.password

    def __str__(self):
        return "Name:"+self.name + "  \nBio: " + self.bio + "  \nEmail: "+self.email
    #picture
    #clubs/roles in clubs



# Create your models here.

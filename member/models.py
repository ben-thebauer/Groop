from django.db import models
class Member(models.Model):
    name = models.CharField(max_length = 100, primary_key=True)
    bio = models.CharField(default="bio goes here", max_length = 500)
    email = models.EmailField('')
    password = models.CharField(max_length=40)
    profile_picture = models.ImageField(default="", upload_to="upload/")

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

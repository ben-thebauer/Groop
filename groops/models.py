from django.db import models

# Create your models here.
class Groop(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    #logo = models.ImageField()
    #website = models.URLField()
    #foreignkey schedule
    #foeignkey members
    #members = models.ForeignKey()
    #Exec = models.foreignKey()

    #CAN ADD ANY CLASS METHODS HERE
    #I THINK YOU CAN TREAT FIELDS LIKE NORMAL SELF.VARIABLES
    def __str__(self):
        return self.name
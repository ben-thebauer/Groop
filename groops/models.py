from django.db import models
from django_mysql.models import ListTextField

#import ast
# Create your models here.

class Groop(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    logo = models.FileField(default="", upload_to="upload/")
    #members = ListTextField(default=[], base_field=models.CharField(max_length=500))
    new_members = ListTextField(default=[], base_field=models.CharField(max_length=500))
    #foreignkey schedule
    #foeignkey members

    #CAN ADD ANY CLASS METHODS HERE
    #I THINK YOU CAN TREAT FIELDS LIKE NORMAL SELF.VARIABLES

    def __str__(self):
        return "{0}".format(self.name)

    def __repr__(self):
        return "Name: {0}\nDescription: {1}\nLogo: {2}\nMembers:{3}".format(self.name,self.description, self.logo, self.new_members)





    # ADMIN FUNCTIONS

    # def is_admin(self, member_name):
    #     for admin in self.admins:
    #         if admin == member_name:
    #             return True
    #     return False
    #
    # def add_admin(self, member_name):
    #     if member_name in self.members and member_name not in self.admins:
    #         self.admins.append(member_name)
    #     else:
    #         print("admins have already be members")
    #
    # def remove_admin(self, admin_name):
    #     if admin_name in self.admins:
    #         self.admins.remove(admin_name)
    #     else:
    #         print("Admin is not in the admin list")
    #
    # # MEMBER FUNCTIONS
    #
    # def add_member(self, new_member):
    #     if new_member not in self.members:
    #         self.members.append(new_member)
    #
    # def remove_member(self, member_name):
    #     if member_name in self.members:
    #         self.members.remove(member_name)
    #     else:
    #         print("Member is not in member list")

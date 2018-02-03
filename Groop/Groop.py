class Groop:

    def __init__(self, new_name, new_admins, new_members, new_description):
        self.name = new_name
        self.admins = new_admins  # list of admins
        self.members = new_members  # list of members
        self.description = new_description

    def __repr__(self):
        return "Name: {0}\nAdmins: {1}\nMembers: {2}\nDescription: {3}".format(self.name,
                                                                           self.admins,
                                                                           self.members,
                                                                           self.description)
    # ADMIN FUNCTIONS

    def is_admin(self, member_name):
        for admin in self.admins:
            if admin == member_name:
                return True
        return False

    def add_admin(self, member_name):
        if member_name in self.members and member_name not in self.admins:
            self.admins.append(member_name)
        else:
            print("admins have already be members")

    def remove_admin(self, admin_name):
        if admin_name in self.admins:
            self.admins.remove(admin_name)
        else:
            print("Admin is not in the admin list")

    # MEMBER FUNCTIONS

    def add_member(self, new_member):
        if new_member not in self.members:
            self.members.append(new_member)

    def remove_member(self, member_name):
        if member_name in self.members:
            self.members.remove(member_name)
        else:
            print("Member is not in member list")

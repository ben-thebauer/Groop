class Member:

    def __init__(self, new_name, new_email):
        self.name = new_name
        self.email = new_email

    def __repr__(self):
        return "Name: {0}\nEmail: {1}".format(self.name, self.email)




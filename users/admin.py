from user import User

"""A module used to represent an Admin"""

class Admin(User):
    """ An attempt to represent an administrator kind of user."""

    def __init__(self, first_name, last_name, age, gender):
        """ Initialize the attributes of the parent class."""
        super().__init__(first_name, last_name, age, gender)
        self.admin_privileges = Priviliges()

class Priviliges():
    """ Represent the privileges an administrator has."""
    
    def __init__(self):
        """ 
        Initialize the attributes to describe
        the privileges an administrator has.
        """ 
        self.priviliges = ["can add post", "can delete post", "can add users",
            "can ban user"]

    def show_priviliges(self):
        """ Print the privileges an administrator has"""
        for privilige in self.priviliges:
            print(privilige)
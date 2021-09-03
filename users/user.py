"""A class that represents a user."""

class User:
    """An attempt to model a user."""
    
    def __init__(self, first_name, last_name, age, gender):
        """Initilize attributes to describe a user."""
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = first_name + " " + last_name
        self.age = age
        self.gender = gender
        self.login_attempts = 0

    def describe_user(self):
        """Print a summary of the user's information."""
        print(f"Name: {self.full_name.title()}")
        # print(f"Name: {self.firts_name.title()} {self.last_name.title()}
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
    
    def greet_user(self):
        """Print a personilized greeting."""
        print(f"Welcome {self.full_name.title()}!")

    def increment_login_attempt(self):
        """Increment the times the user has attempted to log in by one."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the user's number of login attempts.""" 
        self.login_attempts = 0

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
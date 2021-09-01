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

    def describe_user(self):
        """Print a summary of the user's information"""
        print(f"Name: {self.full_name.title()}")
        # print(f"Name: {self.firts_name.title()} {self.last_name.title()}
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
    
    def greet_user(self):
        """Print a personilized greeting"""
        print(f"Welcome {self.full_name.title()}!")
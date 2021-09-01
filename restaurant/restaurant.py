"""A class that can be used to represent a restaurant."""

class Restaurant:
    """ An attempt to represent a restaurant."""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes to describe a restaurant."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Print the reataurant name and its cuisine type."""
        print(f"Restaurant name: {self.restaurant_name.title()}")
        print(f"Cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        """Print a message indicating the restaurant is open.""" 
        print(f"The {self.restaurant_name.title()} restaurant is open")

    def set_number_served(self, number_served):
        """Modify the number of customers that have been served."""
        self.number_served = number_served

    def increment_number_served(self, increment):
        """Increment the number of people that have been served."""
        self.number_served += increment
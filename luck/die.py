from random import randint

class Die:
    """An attempt to represent a die."""

    def __init__(self, number_of_sides):
        """Initialize the attributes of the die class."""
        self.sides = number_of_sides

    def roll_die(self):
        """Roll the die and get a random die's side."""
        side = randint(1, self.sides)
        return(side)


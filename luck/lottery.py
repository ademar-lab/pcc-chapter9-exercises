from random import choice

# Crate a list containing all the possible characters in a lottery
characters = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d"]

def create_ticket():
    """Create a ticket with 4 numbers and/or letters.""" 
    ticket = ""
    for number in range(4):
        random_character = choice(characters)
        if type(random_character) != str:
            ticket += str(random_character)
        else:
            ticket += random_character
    return(ticket)

winner_ticket = create_ticket()
print(f"The ticket matching these four numbers or letters: {winner_ticket}, "
    "wins the prize.")

# Buy a ticket until you win the lottery
num_of_tickets_bought = 0
my_ticket = None
while my_ticket != winner_ticket:
    my_ticket = create_ticket()
    num_of_tickets_bought += 1
print(f"You had to buy: {num_of_tickets_bought} tickets to win.")
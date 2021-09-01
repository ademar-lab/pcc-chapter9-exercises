from restaurant import Restaurant

# Create a instance of the restaurant class
eat_green = Restaurant("eat green", "mediterranean")
print(eat_green.number_served)
eat_green.number_served = 7
print(eat_green.number_served)
eat_green.increment_number_served(21)
print(eat_green.number_served)
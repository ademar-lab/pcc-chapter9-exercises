from user import User

# Create a user instance to represent a real user
user_1 = User("ayrton", "de león vázquez", 19, "male")

# Print and change the user_1's number of login attemps 
print("Number of login attempts:")
print(f"\t{user_1.login_attempts}")
print("\nNumber of login attempts:")
for number in range(1,4):
    user_1.increment_login_attempt()
print(f"\t{user_1.login_attempts}")
user_1.reset_login_attempts()
print("\nNumber of login attempts:")
print(f"\t{user_1.login_attempts}")
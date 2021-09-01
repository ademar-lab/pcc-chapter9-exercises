from user import User

# Create a representation of different users
users = []
user_1 = User("ademar", "de león", 17, "male")
users.append(user_1)
user_2 = User("david", "acosta", 16, "male")
users.append(user_2)
user_3 = User("alejandra", "gonzalez", 16, "female")
users.append(user_3)

for user in users:
    print(f"\nThis is the information about {user.first_name.title()}")
    user.describe_user()
    user.greet_user()
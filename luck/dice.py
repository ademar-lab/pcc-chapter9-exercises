from die import Die

# Create a Die instance
die_1 = Die(6)
die_2 = Die(10)
die_3 = Die(20)

print("Roll a six-sided die ten times:")
for number in range(1, 11):
    print(f"\t{die_1.roll_die()}")
print("\nRoll a ten-sided die ten times:")
for number in range(1, 11):
    print(f"\t{die_2.roll_die()}")
print("\nRoll a twenty-sided die ten times:")
for number in range(1, 11):
    print(f"\t{die_3.roll_die()}")
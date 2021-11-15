print("Welcome to the tip calculator.\n")

total = float(input("What was the total bill? £"))
percentage = int(input("What percentage tip would like? 10, 12 or 15? "))
if percentage == 10:
    tip = float((10 / 100) * total)
elif percentage == 12:
    tip = float((12 / 100) * total)
else:
    tip = float((15 / 100) * total)

people = int(input("How many people to split the bill? "))
each_pays = float(total + tip) / float(people)

print(f"Each person should pay: £{each_pays:.2f}")










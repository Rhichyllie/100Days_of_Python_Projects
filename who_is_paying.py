import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split String Method
everybody = input("Give me everybody´s names, separated by a coma. ")
names = everybody.split(", ")

# Get the total number of names of the list
total = len(names)

# Generate random numbers between 0 and the last index
random_index = random.randint(0, total - 1)

payer = names[random_index]

print(f"{payer} is going to buy the meal today!")
import random
import string

letters = string.ascii_letters
symbols = string.punctuation
numbers = string.digits

print("Welcome to the PyPassword Generator!")
nb_letters = int(input("How many letters would you like in your password?\n"))
nb_symbols = int(input("How many symbols would you like?\n"))
nb_numbers = int(input("How manny number would you like?\n"))

password_list = []

for char in range(1, nb_letters + 1):
    password_list += random.choice(letters)

for char in range(1, nb_symbols + 1):
    password_list += random.choice(symbols)

for char in range(1, nb_numbers + 1):
    password_list += random.choice(numbers)

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")



#Day 3.5
#Take both people´s names and check for the number of times the letters in the word TRUE occurs.
#Them check the number of times the letters LOVE occurs.
#Them combine these numbers to make a 2 or 3 digit number.

print("Welcome to the Love Calculator!")
name1 = input("What is your name? ").lower()
name2 = input("What is their name? ").lower()

combined_string = name1 + name2
#Concatinating the strings

#RegEX(Regular Expression) re.findall(will search fo each
import re
wordTRUE = len(re.findall('[true]', combined_string))
wordLOVE = len(re.findall('[love]', combined_string))
print()

love_score = int(str(wordTRUE) + str(wordLOVE))

if (love_score < 10) or (love_score > 90):
    print(f"Your score {love_score}, you go together are like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"your score {love_score}, you are alright together.")
else:
    print(f"Your score {love_score}.")


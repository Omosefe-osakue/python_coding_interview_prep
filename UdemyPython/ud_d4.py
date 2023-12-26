# A simple random number guessing game

from random import *

name = input("What is your name player: ")
print(f"Hello {name}")

print("Your task is to guess a number between 1 and 100 but you only have 8 tries")

print("\n")

#pick a random number
rando = randint(1,101)

#user input
og_tries=8
tries = 8
while tries > 0:
    tries -= 1
    user_input = int(input("Input your guess: "))
    if (user_input < 1) or (user_input > 100):
        print("Value is out of play")
        continue
    elif(user_input< rando):
        print("Value is less than the number")
        continue
    elif(user_input > rando):
        print("Value is more than the number")
        continue
    elif(user_input == rando):
        print("You have Won")
        print(f"It took you {og_tries-tries} tries to get it")
        break
    else:
        print("You have lost, try again later")
        break
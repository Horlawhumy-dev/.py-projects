# A random guessing game
import random

guessing_range = random.randint(1, 100)

guess = " "

guess_count = 0

guess_limit = 10

time_up = False

while guess != guessing_range and not(time_up):
    if guess_count < guess_limit:
        guess = int(input("Enter the guessing number: "))
        guess_count += 1
    else:
        time_up = True

if time_up:
    print("Oops! Your given time is lapsed.")
else:
    print("Oh! You guessed right.")







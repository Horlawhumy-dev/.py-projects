# A Guessing Game developed by Harof
print("Guess the name of a language that has the following features; Is an object oriented language; Simple and Dynamic; Created around 1990's; Common nowadays in use; Has many IDEs;")
secret_word = "PYTHON"                  # Guessing word
guess = " "                                 # Empty string where to store the user guessing
guess_count = 0                                  # Allowing the user to repeat guessing
guess_limit = 3                                     # Setting limit to the user's guessing
out_of_guesses = False                                  # To check if there are still more guesses
while guess != secret_word and  not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Sorry! Out of Guesses, You lose the game.")
else:
    print("Woow! You win the game.")



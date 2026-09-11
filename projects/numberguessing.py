#number guessing game in python
import random
lower_bound = 1
upper_bound = 100

answer = random.randint(lower_bound, upper_bound)
guesses = 0
is_running = True

while is_running:
    guess = input(f"Guess a number between {lower_bound} and {upper_bound}: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess <lower_bound or guess > upper_bound:
            print(f"Please guess a number between {lower_bound} and {upper_bound}.")
        elif guess < answer:
            print("Too low! Try again.")
        elif guess > answer:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the correct number: {answer}")
            is_running = False
            print(f"your total guesses: {guesses}")
    elif guess.isalpha():
        print("Please enter a valid number.")


    

   
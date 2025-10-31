import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("")

difficulty = input("Choose a difficulty. Type easy (10 chances), medium (5 chances), or hard (3 chances): ")
if difficulty == "easy":
    attempts = 10
elif difficulty == "medium":
    attempts = 5
elif difficulty == "hard":
    attempts = 3
else:
    print("Invalid difficulty selected. Defaulting to easy mode.")
    attempts = 10

print("")

guess = int(input("What number would you like to choose for your guess? "))
number_to_guess = random.randint(1, 100)

while attempts > 0:
    if guess < number_to_guess:
        print("Too low.")
        attempts -= 1
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a new guess: "))
    elif guess > number_to_guess:
        print("Too high.")
        attempts -= 1
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a new guess: "))
    else:
        print(f"You got it! The answer was {number_to_guess}.")
        break
if attempts == 0:
    print("You've run out of guesses, you lose.")
    print(f"The number was {number_to_guess}.")


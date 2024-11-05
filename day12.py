import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ")
if level == "easy":
    attempts = 10
else:
    attempts = 5
correct_number = random.randrange(1, 100)
while True:
    guess_number = int(input("Make a guess: "))
    if guess_number == correct_number:
        print(f"You got it! The answer was {guess_number}")
        break
    if guess_number < correct_number:
        print("Too low.")
        attempts -= 1
    if guess_number > correct_number:
        print("Too high")
        attempts -= 1
    if attempts == 0:
        print("You've run out of guesses, you lose!")
        print(f"The correct number is {correct_number}.")
        break
    print("Guess Again!")
    print(f"You have {attempts} attempts remaining to guess the number.")
    

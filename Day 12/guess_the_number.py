from random import randrange

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

difficulty = input("Choose a difficulity. Type 'easy' or 'hard': ")

random_number = randrange(1, 100)

def choose_difficulty(difficulty):
    if difficulty.lower() == 'easy':
        attempts = 10

    elif difficulty.lower() == 'hard':
        attempts = 5

    else:
        print(f"{difficulty} does not exist. Type in 'easy' or 'hard'")

    print(f"You have {attempts} remaining to guess the number")

    return attempts

def choose_number(guess):

    if guess > random_number:
        print(f"Number {guess} is too High")

    elif guess == random_number:
        print(f"You win! Number was {random_number}!")

    else:
        print(f"Number {guess} is too Low")

    return guess

attempts = choose_difficulty(difficulty=difficulty)

while attempts !=0:
    guess = int(input("Guess a number: "))
    choose_number(guess=guess)

    if guess == random_number:
        break

    attempts -= 1
    print(f"You have {attempts} remaining to guess the number")

print(f"You lose. No more attempts. The number was {random_number}")
import random

list_of_words = ["testing", "baboone", "locomotive"]

generate_word = list_of_words[random.randint(0, len(list_of_words) - 1)]
generate_word.lower()
underscores = []
life = 6


for _ in range(len(generate_word)):
    underscores += "_"

print(underscores)

while "_" in underscores or life != 0:
    ask_letter = input("What letter? " ).lower()

    # Check if single char
    if len(ask_letter) != 1:
        ask_letter = input("Give only a single letter: " ).lower()

    if not ask_letter.isalpha():
        ask_letter = input("Give only a single LETTER: " ).lower()

    # Print _ and Guess
    for position, letter in enumerate(generate_word):

        if letter == ask_letter:
            underscores[position] = ask_letter
            print(underscores)

    if ask_letter not in generate_word:
        life -= 1
        print(life)

    if life == 0:
        print("You've lost!")
        break

    if "_" not in underscores:
        print("You've Won!")
        break
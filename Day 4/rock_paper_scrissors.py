import random

choice = random.randint(0, 3)

player_choice = int(input("Type 0 for Rock, 1 for Paper, 2 for Scissors"))

# 0 - Rock
# 1 - Paper
# 2 = Scrissors

if choice == 0 and player_choice == 1:
    print("Paper beats Rock, You win!")

elif choice == 0 and player_choice == 2:
    print("Rock beats scrissors, Computer wins!")

elif choice == 1 and player_choice == 0:
    print("Paper beats Rock, Computer wins!")

elif choice == 1 and player_choice == 2:
    print("Scissors beats paper, You win!")

elif choice == 2 and player_choice == 0:
    print("Rock beats scrissors, You win!!")

elif choice == 2 and player_choice == 1: 
    print("Scissors beats paper, Computer wins!")

else:
    print("Draw")

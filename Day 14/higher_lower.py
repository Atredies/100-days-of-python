logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

from game_data import data
from random import randrange

SCORE = 0
CONTINUE = True
START =  True
CHOICE  = ('a','b')

def random_generator():
    random_choice = randrange(0, len(data))

    return random_choice

def pick_start_data():
    choice_a = random_generator()

    choice_b = random_generator()

    while choice_a == choice_b:
        choice_b = random_generator()

    compare_a = data[choice_a]['name'], data[choice_a]['description'], data[choice_a]['country']
    compare_b = data[choice_b]['name'], data[choice_b]['description'], data[choice_b]['country']

    count_a = data[choice_a]['follower_count']
    count_b = data[choice_b]['follower_count']

    return count_a, count_b, compare_a, compare_b



def guess():
    global SCORE, CONTINUE, CHOICE, START
    pick_start_data_results = pick_start_data()

    if START:
        count_a = pick_start_data_results[0]
        count_b = pick_start_data_results[1]
        compare_a = pick_start_data_results[2]
        compare_b = pick_start_data_results[3]

    else:
        compare_a = CHOICE[0]
        count_a = CHOICE[1]
        count_b = pick_start_data_results[1]
        compare_b = pick_start_data_results[3]

    print("Compare A: " + compare_a[0] + ", a " + compare_a[1] + ", from " + compare_a[2])
    print(vs)
    print("Against B: " + compare_b[0] + ", a " + compare_b[1] + ", from " + compare_b[2])


    choice = input("Who has more follower? Type 'A' or 'B': ")

    if choice.upper() == 'A':
        if count_a > count_b:
            SCORE += 1
            print(f"You're right! Current score: {SCORE}")
            CONTINUE = True
            CHOICE  = compare_a, count_a

        else:
            print(f"Sorry, that was wrong. Final score: {SCORE}")
            CONTINUE = False

    elif choice.upper() == 'B':
        if count_b > count_a:
            SCORE += 1
            print(f"You're right! Current score: {SCORE}")
            CONTINUE = True
            CHOICE  = compare_b, count_b

        else:
            print(f"Sorry, that was wrong. Final score: {SCORE}")
            CONTINUE = False

    else:
        print("Invalid choice, try again")
        choice = input("Who has more follower? Type 'A' or 'B': ")

    START =  False

    return CHOICE

print(logo)
while CONTINUE:
    guess()
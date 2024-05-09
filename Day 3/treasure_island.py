print("Welcome to Treasure Island. \n Your mission is to find the treasure.")

choice = input("Do you want to go left or right?")

if str(choice).lower() != "left":
    print("Fall into a hole. \n Game Over.")

else:
    choice = input("Swim or wait?")

    if str(choice).lower() != "wait":
        print("Attacked by trout. \n Game Over.")
        

    else:
        choice = input("Which door?")

        if str(choice).lower() == "blue":
            print("Eaten by beasts. \n Game Over.")

        elif str(choice).lower() == "red":
            print("Burned by fire. \n Game Over.")
            
        elif str(choice).lower() == "yellow":
            print("You win!")

        else:
            print("Game over.")
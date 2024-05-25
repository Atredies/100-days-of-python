from coffee_data import MENU
from coffee_data import resources

resources["money"] = 0.00

def what_would_you_like(choice: int):
    if choice == 1:
        coffee = 'espresso'

    elif choice == 2:
        coffee = 'latte'

    elif choice == 3:
        coffee = 'cappuccino'

    else:
        print('Choice is invalid, please choose:\n1: Espresso\n2: Latte\n3: Cappuccino\n')

    return coffee



def process_resources(coffee_type):
    coffee = MENU[coffee_type]
    ingredients = coffee['ingredients']
    coffee_cost = MENU[coffee_type]['cost']

    if coffee_type == 'espresso':
        resources['water'] = resources['water'] - ingredients['water']
        resources['coffee'] = resources['coffee'] - ingredients['coffee']
        resources['money'] = resources['money'] + coffee_cost
    
    else:
        resources['water'] = resources['water'] - ingredients['water']
        resources['coffee'] = resources['coffee'] - ingredients['coffee']
        resources['milk'] = resources['milk'] - ingredients['milk']
        resources['money'] = resources['money'] + coffee_cost





def check_resources(coffee_type):
    coffee = MENU[coffee_type]
    ingredients = coffee['ingredients']

    if coffee_type == 'espresso':
        if ingredients['water'] > resources['water']:
            print("Not enough water to make coffee")
            return False

        if ingredients['coffee'] > resources['coffee']:
            print("Not enough coffee to make coffee")
            return False
    
    else:
        if ingredients['water'] > resources['water']:
            print("Not enough water to make coffee")
            return False

        if ingredients['coffee'] > resources['coffee']:
            print("Not enough coffee to make coffee")
            return False
        
        if ingredients['milk'] > resources['milk']:
            print("Not enough water to make coffee")
            return False



def process_coints(coffee_type):
    refund_opt = False
    coin_count = 0.00
    coffee_cost = MENU[coffee_type]['cost']

    while coin_count < coffee_cost:
        insert_coin = int(input("Please add coins:\n1. Quarter\n2. Dime\n3. Nickle\n4. Penny\n5. Refund\nChoice: "))

        if insert_coin == 1:
            coin_count += 0.25

        elif insert_coin == 2:
            coin_count += 0.1

        elif insert_coin == 3:
            coin_count += 0.05

        elif insert_coin == 4:
            coin_count += 0.01

        elif insert_coin == 5:
            rounded_coin_count = round(coin_count, 2)
            print(f"Opted for refund. Returing {rounded_coin_count}")
            refund_opt = True
            break

        else:
            print("Option not valid, please choose a valid option")

        rounded_coin_count = round(coin_count, 2)
        print(f"Credit: {rounded_coin_count}")

    if refund_opt:
        pass

    else:
        print("Enough credit to make the coffee")
        rest = coin_count - coffee_cost
        rounded_change = round(rest, 2)

        print(f"Returning your change: {rounded_change}")
    
    return refund_opt




def choose_type_of_operation(system_type):
    if system_type == 1:
        coffee_type = what_would_you_like(int(input('What kind of coffe would you like:\n1: Espresso\n2: Latte\n3: Cappuccino\nChoice: ')))

        if check_resources(coffee_type) == False:
            print("Not enough ingredients to make the coffee, please choose something else")

        else:
            print("Enough ingredients to make the coffee")
            refund_opt = process_coints(coffee_type)
            process_resources(coffee_type)

            if refund_opt:
                pass

            else:
                print("Here is your latte. Enjoy!")
    

    elif system_type == 2:
        print("Water: " + str(resources['water']))
        print("Milk: " + str(resources['milk']))
        print("Coffee: " + str(resources['coffee']))
        print("Money: " + str(resources['money']))



    elif system_type == 3:
        print('Machine turning off...')
        exit()

    else:
        print(f"{system_type} is not a valid option. Returning to main menu.")


while True:
    choose_type_of_operation(int(input('Main menu:\n1. Coffee\n2. Report\n3. Turn off\nChoice:')))
    
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_on = True

while is_on:
    menu_option_number = int(input("Select a number:\n1. Coffee\n2. Report\n3. Money Report\n4. Shut Down\nChoice: "))
    if menu_option_number == 1:
        print(menu.get_items())
        coffee_type = input("What kind of coffee do you want?:\n")

        find_drink = menu.find_drink(coffee_type)

        if coffee_maker.is_resource_sufficient(find_drink):
            payment = money_machine.make_payment(find_drink.cost)

            if payment:
                coffee_maker.make_coffee(find_drink)


    elif menu_option_number == 2:
        print(coffee_maker.report())


    elif menu_option_number == 3:
        print(money_machine.report())

    elif menu_option_number == 4:
        print("Shutting down....")
        is_on = False

    else:
        print("Option not available")

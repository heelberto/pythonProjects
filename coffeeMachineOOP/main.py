from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def user_prompt():

    power = True
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    while power:
        choice = input(f"What would you like?({menu.get_items()}):")
        if choice == 'off':
            break
        elif choice == 'report':
            coffee_maker.report()
            money_machine.report()
        else:
            choice_object = menu.find_drink(choice)
            for ingredient,value in choice_object.ingredients.items():
                print(f"{ingredient}:{value}")
            if coffee_maker.is_resource_sufficient(choice_object):
                print("There's sufficient resources for your drink")
                money_machine.make_payment(choice_object.cost)
                coffee_maker.make_coffee(choice_object)
            else:
                print("There's NOT sufficient resources for your drink")

    print("...POWERING OFF...")


user_prompt()
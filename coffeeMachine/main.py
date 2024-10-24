import menu

machine_balance = 0.0


def make_drink(drink):
    if drink == "espresso":
        menu.resources["water"] -= menu.MENU[drink]["ingredients"]["water"]
        menu.resources["coffee"] -= menu.MENU[drink]["ingredients"]["coffee"]
    elif drink == "latte":
        menu.resources["water"] -= menu.MENU[drink]["ingredients"]["water"]
        menu.resources["coffee"] -= menu.MENU[drink]["ingredients"]["coffee"]
        menu.resources["milk"] -= menu.MENU[drink]["ingredients"]["milk"]
    elif drink == "cappuccino":
        menu.resources["water"] -= menu.MENU[drink]["ingredients"]["water"]
        menu.resources["coffee"] -= menu.MENU[drink]["ingredients"]["coffee"]
        menu.resources["milk"] -= menu.MENU[drink]["ingredients"]["milk"]
    else:
        return


def user_prompt():
    choice = input("what would you like? (espresso/latte/cappuccino): ").lower()

    #resource_check(choice)

    if choice == "espresso":
        return choice
    elif choice == "latte":
        return choice
    elif choice == "cappuccino":
        return choice
    elif choice == "off":
        return choice
    elif choice == "report":
        print_resources()
        return choice
    else:
        print("Error: not a valid choice")


def print_resources():
    water_quantity = menu.resources["water"]
    milk_quantity = menu.resources["milk"]
    coffee_quantity = menu.resources["coffee"]
    current_machine_balance = machine_balance

    print(f"Water: {water_quantity}ml\n"
          f"Milk: {milk_quantity}ml\n"
          f"Coffee: {coffee_quantity}g\n"
          f"Money: ${current_machine_balance}\n")


def resource_check(drink):
    water_quantity = menu.resources["water"]
    milk_quantity = menu.resources["milk"]
    coffee_quantity = menu.resources["coffee"]

    water_requirement = 0
    milk_requirement = 0
    coffee_requirement = 0

    if drink == "espresso":
        water_requirement = menu.MENU[drink]["ingredients"]["water"]
        coffee_requirement = menu.MENU[drink]["ingredients"]["coffee"]
        if water_requirement > water_quantity:
            print("Not enough water!\n~~Please refill water~~")
            return False
        if coffee_requirement > coffee_quantity:
            print("Not enough coffee\n~~Please refill coffee~~")
            return False
        return True
    elif drink == "latte":
        water_requirement = menu.MENU[drink]["ingredients"]["water"]
        milk_requirement = menu.MENU[drink]["ingredients"]["milk"]
        coffee_requirement = menu.MENU[drink]["ingredients"]["coffee"]
        if water_requirement > water_quantity:
            print("Not enough water!\n~~Please refill water~~")
            return False
        if coffee_requirement > coffee_quantity:
            print("Not enough coffee\n~~Please refill coffee~~")
            return False
        if milk_requirement > milk_quantity:
            print("Not enough milk\n~~Please refill milk")
            return False
        return True
    elif drink == "cappuccino":
        water_requirement = menu.MENU[drink]["ingredients"]["water"]
        milk_requirement = menu.MENU[drink]["ingredients"]["milk"]
        coffee_requirement = menu.MENU[drink]["ingredients"]["coffee"]
        if water_requirement > water_quantity:
            print("Not enough water!\n~~Please refill water~~")
            return False
        if coffee_requirement > coffee_quantity:
            print("Not enough coffee\n~~Please refill coffee~~")
            return False
        if milk_requirement > milk_quantity:
            print("Not enough milk\n~~Please refill milk")
            return False
        return True
    elif drink == "report":
        return
    else:
        print("Error: drink not on the menu!")


def process_coins(drink):
    if drink == "report":
        return
    global machine_balance
    drink_cost = menu.MENU[drink]["cost"]
    amount_owed = drink_cost
    change = 0

    print(f"{drink}'s cost: {drink_cost}\n")
    while drink_cost > 0:
        print(f"Amount owed: ${drink_cost}")
        current_coin = int(input("Enter choice:\n"
                             "[1] quarter: $0.25\n"
                             "[2] dime: $0.10\n"
                             "[3] nickel: $0.05\n"
                             "[4] penny: $0.01\n"))
        if current_coin == 1:
            drink_cost -= 0.25
            if drink_cost < 0:
                change = abs(drink_cost)
                print(f"your change = $ {change}")
        elif current_coin == 2:
            drink_cost -= 0.1
            if drink_cost < 0:
                change = abs(drink_cost)
                print(f"your change = $ {change}")
        elif current_coin == 3:
            drink_cost -= 0.05
            if drink_cost < 0:
                change = abs(drink_cost)
                print(f"your change = $ {change}")
        elif current_coin == 4:
            drink_cost -= 0.01
            if drink_cost < 0:
                change = abs(drink_cost)
                print(f"your change = $ {change}")
        else:
            print("error: not a valid coin option!")
    print("Successfully payed cost")
    machine_balance += amount_owed


def main():

    power = True
    enough_resources = True
    while power:
        choice = user_prompt()
        if choice == "off":
            power = False
            break
        enough_resources = resource_check(choice)

        if enough_resources:
            process_coins(choice)
            make_drink(choice)
            print(f"Here's your {choice}. Enjoy!")

    print("...Machine shut down process initiated...")


if __name__ == '__main__':
    main()

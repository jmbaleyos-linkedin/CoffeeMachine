import data
from art import logo

def print_report_status():
    print(f"Water: {data.resources["water"]}ml")
    print(f"Milk: {data.resources["milk"]}ml")
    print(f"Coffee: {data.resources["coffee"]}g")

def print_menu():
    print("Available coffees:")
    for menu in data.MENU.keys():
        print(f"- {menu.title()} : ${data.MENU[menu]['cost']}")

def integer_checker(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Please input a number only.")

def coins_inserted_checker(coffee_cost):
    total_inserted_coins = 0
    print(F"Please insert ${coffee_cost}.")
    while True:
        total_inserted_coins += integer_checker("How many quarters? ") * 0.25
        if remaining_balance(total_inserted_coins, coffee_cost):
            break
        total_inserted_coins += integer_checker("How many dimes? ") * 0.10
        if remaining_balance(total_inserted_coins, coffee_cost):
            break
        total_inserted_coins += integer_checker("How many nickles? ") * 0.05
        if remaining_balance(total_inserted_coins, coffee_cost):
            break
        total_inserted_coins += integer_checker("How many pennies? ") * 0.01
        if remaining_balance(total_inserted_coins, coffee_cost):
            break

def remaining_balance(total_inserted_coins, coffee_name):
    if total_inserted_coins < coffee_name:
        print(f"Please insert more coins for the remaining ${coffee_name - total_inserted_coins}")
        return False
    elif total_inserted_coins > coffee_name:
        print(f"You inserted more. You have ${total_inserted_coins - coffee_name} change.")
        return True
    else:
        print("You inserted exact amount")
        return True

def dispense_coffee(coffee_name):
    print(f"{coffee_name.title()} would cost ${data.MENU[coffee_name]['cost']}.")
    coins_inserted_checker(data.MENU[coffee_name]['cost'])
    for ingredient, need in data.MENU[coffee_name]["ingredients"].items():
        data.resources[ingredient] = data.resources.get(ingredient, 0) - data.MENU[coffee_name]["ingredients"][ingredient]
    print("Thank you for ordering! Grab your change and enjoy your coffee.")

def resources_checker(coffee_name):
    missing_ingredient = False
    for ingredient, need in data.MENU[coffee_name]["ingredients"].items():
        have = data.resources.get(ingredient, 0)
        if have < need:
            missing_ingredient = True
            print(f"Not enough {ingredient}. Please refill")
    if missing_ingredient:
        return False
    else:
        return True

def refill_resources():
    for resource in data.resources.keys():
        data.resources[resource] += integer_checker(f"How much {resource} are you gonna fill? ")

print(logo)
continue_running = True
total_earnings = 0
while continue_running:
    print_menu()
    while True:
        user_input = input("What coffee is you like? ").strip().lower()
        match user_input:
            case "espresso":
                if resources_checker("espresso"):
                    dispense_coffee("espresso")
                    total_earnings += data.MENU["espresso"]["cost"]
                else:
                    print(f"Sorry, Espresso is not available. Please pick other coffee.")
            case "latte":
                if resources_checker("latte"):
                    dispense_coffee("latte")
                    total_earnings += data.MENU["latte"]["cost"]
                else:
                    print(f"Sorry, Latte is not available. Please pick other coffee.")
            case "cappuccino":
                if resources_checker("cappuccino"):
                    dispense_coffee("cappuccino")
                    total_earnings += data.MENU["cappuccino"]["cost"]
                else:
                    print(f"Sorry, Cappuccino is not available. Please pick other coffee.")
            case "refill":
                refill_resources()
            case "menu":
                print_menu()
            case "report":
                print_report_status()
            case "bank":
                print(f"Current total in the bank is: ${total_earnings}.")
            case "off":
                print("Goodbye! Shutting down.")
                continue_running = False
                break
            case _:
                print("Please enter only what's in the menu.")
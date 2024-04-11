from random import randint

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}
resources = {
    "water": randint(0, 1000),
    "milk": randint(0, 1000),
    "coffee": randint(0, 1000),
}

coffee_nums = {"1": "espresso", "2": "latte", "3": "cappuccino"}


def greeting():
    print("Welcome! What drink would you like to have today?\n")
    print("Print 1 for espresso; 2 for latte; 3 for cappuccino\n")


greeting()


def ask_for_a_drink() -> str:
    while True:
        coffee_choice = input("Choose 1, 2 or 3: ")
        if coffee_choice in coffee_nums.keys():
            print(f"You've chosen option for coffee is: {coffee_nums[coffee_choice]}")
            return coffee_choice
        else:
            print(
                "Invalid choice. Please choose 1 for espresso; 2 for latte; 3 for cappuccino\n"
            )


user_coffee_choice = ask_for_a_drink()


def check_resourses(user_coffee_choice):
    drink_name = coffee_nums[user_coffee_choice]
    drink_ingridients = MENU[drink_name]["ingredients"]

    for ingridient, amount_required in drink_ingridients.items():
        if resources[ingridient] < amount_required:
            print(f"Sorry, there is not enough {ingridient} for {drink_name}.")
            return False
        else:
            return True


are_there_enough_resourses = check_resourses(user_coffee_choice)

coins_in_the_machine = {
    "quarters": 50,
    "dimes": 50,
    "nickles": 50,
    "pennies": 50,
}
print(f"coins_in_the_machine: {coins_in_the_machine}")


def process_coins_until_enough_inserted(user_coffee_choice):
    drink_name = coffee_nums[user_coffee_choice]
    price_for_chosen_drink = MENU[drink_name]["cost"]
    print(f"{drink_name} costs ${price_for_chosen_drink}. Please insert coins.")

    total_inserted = 0

    while total_inserted < price_for_chosen_drink:
        if total_inserted > 0:
            print(
                f"Current amount inserted: ${total_inserted:.2f}. Please insert additional coins to reach ${price_for_chosen_drink}."
            )

        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))

        # Update total inserted
        total_inserted += (
            quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
        )

        if total_inserted >= price_for_chosen_drink:
            # Update the coins in the machine
            coins_in_the_machine["quarters"] += quarters
            coins_in_the_machine["dimes"] += dimes
            coins_in_the_machine["nickles"] += nickles
            coins_in_the_machine["pennies"] += pennies

            # Update total sum of coins in the machine
            print(f"Total amount inserted: ${total_inserted:.2f}.")
            return total_inserted
        else:
            print(
                f"Not enough money. You have inserted ${total_inserted:.2f}, but {drink_name} costs ${price_for_chosen_drink}."
            )
            more_coins_answer = input("Do you want to add more coins? [y/n]: ")
            if more_coins_answer.lower() != "y":
                print(
                    f"Transaction cancelled. Returning coins back. Here is your ${total_inserted:.2f}"
                )
                return 0


user_coins = process_coins_until_enough_inserted(user_coffee_choice)
print(f"COINS AFTER INSERT: {coins_in_the_machine}")


def calculate_change(user_coins):
    drink_name = coffee_nums[user_coffee_choice]
    price_for_chosen_drink = MENU[drink_name]["cost"]
    change = user_coins - price_for_chosen_drink
    change_in_cents = round(change * 100)

    number_of_quarters_to_give_back = change_in_cents // 25
    remaining_cents = change_in_cents % 25

    number_of_dimes_to_give_back = remaining_cents // 10
    remaining_cents %= 10

    number_of_nickles_to_give_back = remaining_cents // 5
    remaining_cents %= 5

    number_of_pennies_to_give_back = int(remaining_cents)

    return {
        "quarters": int(number_of_quarters_to_give_back),
        "dimes": int(number_of_dimes_to_give_back),
        "nickles": int(number_of_nickles_to_give_back),
        "pennies": int(number_of_pennies_to_give_back),
    }


dict_of_coins_to_return = calculate_change(user_coins)


def updating_coins_in_the_machine(
    coins_in_the_machine,
    dict_of_coins_to_return,
):
    for coin_type, num_to_return in dict_of_coins_to_return.items():
        coins_in_the_machine[coin_type] -= num_to_return
    return coins_in_the_machine


updated_coins_in_the_machine = updating_coins_in_the_machine(
    coins_in_the_machine, dict_of_coins_to_return
)
print(f"Coins after giving change back = {coins_in_the_machine}")

from machine import MENU, coffee_nums, coins_in_the_machine, resources
from services import (
    ask_for_a_drink,
    calculate_change,
    check_resourses,
    greeting,
    process_coins_until_enough_inserted,
    updating_coins_in_the_machine,
)

if __name__ == "__main__":
    coins_in_current_machine = coins_in_the_machine
    greeting()
    user_coffee_choice = ask_for_a_drink(coffee_nums)
    drink_name = coffee_nums[user_coffee_choice]
    are_there_enough_resourses = check_resourses(drink_name, MENU, resources)
    if are_there_enough_resourses is True:
        print(f"coins_in_the_machine in the beginning: {coins_in_current_machine}")
        user_coins = process_coins_until_enough_inserted(
            drink_name, coins_in_current_machine, MENU
        )
        print(f"COINS AFTER INSERT: {coins_in_current_machine}")
        dict_of_coins_to_return = calculate_change(
            user_coins,
            drink_name,
            MENU,
        )
        updating_coins_in_the_machine(
            coins_in_current_machine,
            dict_of_coins_to_return,
        )
        print(f"Here is your change and ({drink_name})")

from coffee_maker import CoffeeMaker
from menu import Menu, MenuItem
from money import MoneyMachine

if __name__ == "__main__":
    our_money_machine = MoneyMachine()
    our_cofee_maker = CoffeeMaker()
    our_menu = Menu()

    our_cofee_maker.report()
    our_money_machine.report()

    choice = our_cofee_maker.user_cofee_choice()
    if choice is not False:
        drink_menu_object = our_menu.find_drink(choice)
        if our_cofee_maker.is_resource_sufficient(drink_menu_object):
            print(f"{choice} costs ${drink_menu_object.cost}")
            if our_money_machine.make_payments(drink_menu_object.cost):
                our_cofee_maker.make_coffee(drink_menu_object)
                our_money_machine.report()
                our_cofee_maker.report()

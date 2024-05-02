from coffee_maker import CoffeeMaker
from menu import Menu, MenuItem
from money import MoneyMachine

if __name__ == "__main__":
    our_money_machine = MoneyMachine()
    our_cofee_maker = CoffeeMaker()

    our_cofee_maker.report()
    our_money_machine.report()

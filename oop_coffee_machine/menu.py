from random import randint


class MenuItem:
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingridients = {"water": water, "milk": milk, "coffee": coffee}


class Menu:
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappucino", water=250, milk=50, coffee=24, cost=3),
        ]


class ResourcesItem:
    def __init__(self, water, milk, coffee):
        self.resources = {
            water: randint(0, 1000),
            milk: randint(0, 1000),
            coffee: randint(0, 1000),
        }

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
coins_in_the_machine = {
    "quarters": 10,
    "dimes": 10,
    "nickles": 20,
    "pennies": 20,
}
coffee_nums = {"1": "espresso", "2": "latte", "3": "cappuccino"}
resources = {
    "water": randint(0, 1000),
    "milk": randint(0, 1000),
    "coffee": randint(0, 1000),
}

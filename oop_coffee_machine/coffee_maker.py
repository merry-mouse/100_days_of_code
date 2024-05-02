from random import randint


class CoffeeMaker:
    def __init__(self):
        self.resources = {
            "water": randint(0, 1000),
            "milk": randint(0, 1000),
            "coffee": randint(0, 1000),
        }

    def report(self):
        """Prints report of all resources"""
        for resource, amount in self.resources.items():
            print(f"{resource}: {amount} ml/g")

    def is_resource_sufficient(self, drink):
        """Returns True when order is possible"""
        can_make = True
        for item in drink.ingridients:
            if drink.ingridients[item] > self.resources[item]:
                print(f"Sorry, there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """Deducts required ingridients from the resources."""
        for item in order.ingridients:
            self.resources[item] -= order.ingridients[item]
        print(f"Here is your {order.name}. Enjoy!")

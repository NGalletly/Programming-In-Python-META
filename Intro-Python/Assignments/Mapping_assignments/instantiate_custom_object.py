class Recipe:
    def __init__(self, dish, items, time):
        self.dish = dish
        self.items = items
        self.time = time

    def contents(self):
        print(
            "The "
            + str(self.dish)
            + " has "
            + str(self.items)
            + " and takes "
            + str(self.time)
            + " mins to prepare."
        )


pizza = Recipe("pizza", ["cheese", "sauce", "dough"], 45)
pasta = Recipe("pasta", ["penne", "sauce", "garlic"], 5)

print(pizza.items)
print(pizza.contents())
print(pasta.items)
print(pasta.contents())

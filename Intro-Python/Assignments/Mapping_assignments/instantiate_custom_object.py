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


# class MyFirstClass:
#     print("Who wrote this?")
#     index = "Author-Book"

#     def hand_list(self, philosopher, book):
#         print(philosopher + " wrote the book: " + book)


# whodunnit = MyFirstClass()

# whodunnit.hand_list("sun - tzu", "art of war")


class MyFirstClass:
    index = "Author-Book"

    def __init__(self):
        print("Who wrote this?")  # Move the print statement into the constructor

    def hand_list(self, philosopher, book):
        print(MyFirstClass.index)
        print(philosopher + " wrote the book: " + book)


# Instantiate the class
whodunnit = MyFirstClass()
# Call the method with parameters
# whodunnit.hand_list("Sun Tzu", "The Art of War")

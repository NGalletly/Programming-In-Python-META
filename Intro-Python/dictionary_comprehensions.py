# # Using range() function and no input list
# usingrange = {x:x*2 for x in range(12)}
# print("Using range(): ",usingrange)

# # Lists
# months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
# number = [1,2,3,4,5,6,7,8,9,10,11,12]

# # Using one input list
# numdict = {x:x**2 for x in number}
# print("Using one input list to create dict: ", numdict)

# # Using two input lists
# months_dict = {key:value for (key, value) in zip(number, months)}
# print("Using two lists: ", months_dict)

# ---------------------------------------------------------------------
# CHALLENGE 1: The Square Dictionary (Dict)
# Given the list of numbers below, create a dictionary where the keys
# are the numbers themselves, and the values are the squares of those numbers.
#
# Expected Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# ---------------------------------------------------------------------
numbers = [1, 2, 3, 4, 5]

# Your code here:
# dict_task_1 = 
squared_comprehension_dict = {x:x**2 for x in numbers}
print("squared numbers:", squared_comprehension_dict)

# ---------------------------------------------------------------------
# CHALLENGE 2: Stock Price Filter (Dict)
# Given a dictionary of items and their prices, write a dictionary 
# comprehension that filters the data to ONLY keep items that cost 
# strictly more than $100.
# Hint: To loop through a dict, use `.items()` like: `for item, price in stock.items()`
#
# Expected Output: {'Laptop': 1200, 'Monitor': 250}
# ---------------------------------------------------------------------
stock = {"Laptop": 1200, "Mouse": 25, "Monitor": 250, "Keyboard": 45}

# Your code here:
# dict_task_2 = 

dict_price_filter = {key:value for key, value in stock.items() if value > 100}
print(dict_price_filter)

# CHALLENGE 3: The Case Converter (Dict)
# Given a dictionary mapping usernames to their status, write a dictionary 
# comprehension that creates a NEW dictionary where all the username keys 
# are converted to lowercase, but the status values stay exactly the same.
# Hint: Use `key.lower()` to change string casing.
#
# Expected Output: {'alice': 'admin', 'bob': 'user', 'charlie': 'user'}
# ---------------------------------------------------------------------
users = {"Alice": "admin", "Bob": "user", "Charlie": "user"}

# Your code here:
# dict_task_3 = 
lowercase_users = {key.lower():value for key, value in users.items()}
print(lowercase_users)

# ---------------------------------------------------------------------
# CHALLENGE 4: Name Length Map (Dict)
# Given a list of programming languages, write a dictionary comprehension 
# that turns the list into a dictionary. The keys should be the language 
# names, and the values should be the integer length of each name.
# Hint: Loop over the list normally (`for lang in languages`), and use `len(lang)`.
#
# Expected Output: {'python': 6, 'c': 1, 'java': 4, 'golang': 6}
# ---------------------------------------------------------------------
languages = ["python", "c", "java", "golang"]

# Your code here:
# dict_task_4 =
lang_dictionary = {items: len(items) for items in languages}
print(lang_dictionary)













# ---------------------------------------------------------------------
# CHALLENGE 3: The Duplicate Eraser (Set)
# Given a list of cities that contains duplicates and messy capitalization,
# write a SET comprehension that converts all names to lowercase.
# (Because it's a set, it should automatically remove any duplicate results!)
#
# Expected Output: {'london', 'paris', 'tokyo'}  Note: Sets are unordered!
# ---------------------------------------------------------------------
# dirty_cities = ["London", "Paris", "london", "Tokyo", "PARIS", "London"]

# Your code here:
# set_task_3 = 


# ---------------------------------------------------------------------
# CHALLENGE 4: Even Lengths Only (Set)
# Given the list of words below, write a SET comprehension that calculates 
# the length of each word, but ONLY if the length of that word is an even number.
# Hint: Use `len(word)`.
#
# Expected Output: {4, 6} (from 'java' which is 4, and 'python'/'golang' which are 6)
# ---------------------------------------------------------------------
# words = ["python", "java", "c", "html", "golang"]

# Your code here:
# set_task_4 =
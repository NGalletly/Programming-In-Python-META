# data = [2,3,5,7,11,13,17,19,23,29,31]

# # Ex1: List comprehension: updating the same list
# data = [x+3 for x in data]
# print("Updating the list: ", data)

# # Ex2: List comprehension: creating a different list with updated values
# new_data = [x*2 for x in data]
# print("Creating new list: ", new_data)

# # Ex3: With an if-condition: Multiples of four:
# fourx = [x for x in new_data if x%4 == 0 ]
# print("Divisible by four", fourx)

# # Ex4: Alternatively, we can update the list with the if condition as well
# fourxsub = [x-1 for x in new_data if x%4 == 0 ]
# print("Divisible by four minus one: ", fourxsub)

# # Ex5: Using range function:
# nines = [x for x in range(100) if x%9 == 0]
# print("Nines: ", nines)

# CHALLENGE 1: The Prime Decrementer
# Given the list of primes below, write a list comprehension that subtracts 1 
# from every number, but ONLY if the number is greater than 10. 
# (Numbers 10 or less should be completely left out of the new list).
#
# Expected Output: [10, 12, 16, 18, 22, 28, 30]
# ---------------------------------------------------------------------
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

# Your code here:
# task_1 = 

prime_decremeter = [x-1 for x in primes if x>9]
print("Prime decremeter", prime_decremeter)


# ---------------------------------------------------------------------
# CHALLENGE 2: The Length Filter
# Given the list of programming languages below, write a list comprehension 
# that only keeps languages whose names are strictly longer than 5 characters.
#
# Expected Output: ['python', 'javascript', 'golang']
# ---------------------------------------------------------------------
languages = ["python", "c", "java", "javascript", "html", "golang", "rb"]

# Your code here:
# task_2 = 
lng_greater_five =  [x for x in languages if len(x)>4]
print("Length greater than five", lng_greater_five)

# ---------------------------------------------------------------------
# CHALLENGE 3: The Data Normalizer (If-Else)
# Given the list of temperature readings, some are strings and some are integers.
# Write a list comprehension that converts any string digits into actual integers, 
# while leaving existing integers alone. 
# Hint: Use `int(x)` for the conversion and `type(x) == str` or `isinstance(x, str)` to check.
#
# Expected Output: [22, 25, 19, 24, 21, 26]
# ---------------------------------------------------------------------
readings = [22, "25", 19, "24", 21, "26"]

# Your code here:
# task_3 = [value_if_true if condition else value_if_false for item in iterable]
# int_list = [int(x) if type(x)!= int else x for x in readings]
# print("integer list", int_list)
# def return_type(list):
#     list_copy = list.copy()
#     i=0
#     for i in range(len(list)):
#         if type(i) == int:
#             list_copy[i] = True
#             i+=1
#     return list_copy

# print(return_type(readings))


# ---------------------------------------------------------------------
# CHALLENGE 4: The Vowel Stripper
# Given a string, write a list comprehension that extracts every character 
# EXCEPT for vowels (a, e, i, o, u). 
# Hint: Strings are iterable just like lists! You can check `if char not in "aeiou"`.
#
# Expected Output: ['p', 'y', 't', 'h', 'n']
# ---------------------------------------------------------------------
word = "python"

# Your code here:
# task_4 = 
# remove_vowels = [x for x in word if x not in "aeiou"]
# print(remove_vowels)
# ---------------------------------------------------------------------
# CHALLENGE 5: Matrix Filter (Advanced)
# Given a 2D matrix (a list of sublists), write a nested list comprehension 
# to flatten it into a single 1D list, but ONLY keep numbers that are multiples of 3.
#
# Expected Output: [3, 6, 9, 12]
# ---------------------------------------------------------------------
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

# Your code here:
# task_5 =
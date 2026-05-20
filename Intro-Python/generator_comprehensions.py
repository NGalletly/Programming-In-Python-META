data = [2,3,5,7,11,13,17,19,23,29,31]
gen_obj = (x for x in data)
print(gen_obj)
print(type(gen_obj))
for items in gen_obj:
    print(items, end=" ")

print("\n--- Second Loop ---")

for items in gen_obj:
    print(items, end=" ")


# =====================================================================
# PYTHON GENERATOR EXPRESSION CHALLENGES
# Try to solve each one using a single-line generator expression ( ).
# =====================================================================

# ---------------------------------------------------------------------
# CHALLENGE 1: The Lazy Upper-Caser
# Create a generator expression that takes the list of words below and 
# converts them to uppercase. 
# Then, use the next() function twice to manually print just the first two words.
#
# Expected Output when running next() twice:
# PYTHON
# JAVASCRIPT
# ---------------------------------------------------------------------
words = ["python", "javascript", "c++", "java"]

# Your code here:
# gen_task_1 = 
gen_words = (x.upper() for x in words)
print(next(gen_words))
print(next(gen_words))


# ---------------------------------------------------------------------
# CHALLENGE 2: The Countdown Stream
# Given a range of numbers from 10 down to 1, create a generator expression 
# that yields each number. Then, write a for loop to print them all on 
# a single line separated by spaces.
# Hint: range(10, 0, -1) counts down from 10 to 1. Remember `end=" "`.
#
# Expected Output: 10 9 8 7 6 5 4 3 2 1 
# ---------------------------------------------------------------------

# Your code here:
# gen_task_2 = 
gen_countdown = (x for x in range(10,0,-1))
for x in gen_countdown:
    print(x, end=" ")

print()

# ---------------------------------------------------------------------
# CHALLENGE 3: Memory-Efficient Filter
# Imagine you have a massive list of numbers. Create a generator expression 
# that only yields numbers from the list that are multiples of 5.
# Loop through your generator to print the results on one line.
#
# Expected Output: 5 10 15 20 25 30 
# ---------------------------------------------------------------------
huge_dataset = [2, 5, 7, 10, 11, 15, 18, 20, 22, 25, 29, 30, 33]

# Your code here:
# gen_task_3 =
multiples_five = (x for x in huge_dataset if x % 5 == 0)
for item in multiples_five:
    print(item, end = " ")


print()

a = [[96], [69]]

print(''.join(list(map(str, a))))
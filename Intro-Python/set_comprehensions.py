set_a = {x for x in range(10,20) if x not in [12,14,16]}
print(set_a)

# =====================================================================
# PYTHON SET COMPREHENSION CHALLENGES
# Try to solve each one using a single-line comprehension.
# =====================================================================

# ---------------------------------------------------------------------
# CHALLENGE 1: The Duplicate Eraser
# Given a list of cities with sloppy capitalization and duplicates,
# write a set comprehension that forces all names to lowercase.
# (Because it's a set, it should automatically leave you with unique names!)
#
# Expected Output: {'london', 'paris', 'tokyo'}  (Note: Sets are unordered!)
# ---------------------------------------------------------------------
dirty_cities = ["London", "Paris", "london", "Tokyo", "PARIS", "London"]

# Your code here:
# set_task_1 = 
city_lowercase = {x.lower() for x in dirty_cities}
print(city_lowercase)


# ---------------------------------------------------------------------
# CHALLENGE 2: Even Lengths Only
# Given the list of words below, write a set comprehension that calculates 
# the length of each word, but ONLY if the length of that word is an even number.
# Hint: Use `len(word)` and the modulo operator `%`.
#
# Expected Output: {4, 6} 
# (Explanation: 'java' & 'html' are 4. 'python' & 'golang' are 6. 
#  'c' is 1, so it gets dropped. The duplicates disappear!)
# ---------------------------------------------------------------------
words = ["python", "java", "c", "html", "golang"]

# Your code here:
# set_task_2 = 
even_len = {len(x) for x in words if len(x) % 2 ==0}
print(even_len)


# ---------------------------------------------------------------------
# CHALLENGE 3: Vowel Finder
# Given a sentence string, write a set comprehension that extracts all 
# the unique vowels present in the sentence, forced to lowercase.
# Hint: You can iterate over a string directly: `for char in sentence`. 
# Remember to check if it's a vowel!
#
# Expected Output: {'e', 'a', 'o', 'u'} (Order doesn't matter)
# ---------------------------------------------------------------------
sentence = "The quick brown fox jumps over the lazy dog"

# Your code here:
# set_task_3 =

vowel_finder = {x for x in sentence if x in "aeiou"}
print(vowel_finder)
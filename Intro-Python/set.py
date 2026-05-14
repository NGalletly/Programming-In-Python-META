set_a = {1,2,3,4,5}

print(set_a)

# Sets differ from lists as they do not allow duplicate values. The extra 5's are not printed

set_b = {1,2,3,4,5,5,5}

print(set_b)

set_a.add(6)

print(set_a)

set_a.remove(6)

print(set_a)

set_a.discard(2)

print(set_a)

set_c = {4,5,6,7,8,9}

# You can join sets together with union keyword:

print(set_a.union(set_c))

# Can also use the | operator to join sets

print(set_a | set_c)

# You can also use intersectionto show only values which exist in both sets
print(set_a.intersection(set_c))
# You can also use & symbol for the same result:
print(set_a & set_c)

# You can use difference inbuilt function to print the values of set 1 that are not found in set 2
print(set_a.difference(set_c)) 

# To find the difference in both sets you can use symmetric_difference:
print(set_a.symmetric_difference(set_c))
# This can also be represented by the karat operator(^)
print(set_a ^ set_c)

# A set is a collection with no duplicates BUT it is also a collection of unordered items.
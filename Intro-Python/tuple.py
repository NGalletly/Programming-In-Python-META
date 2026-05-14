#Tuples are immutable

my_tuple = (1,'strings', 4.5, True)
print(my_tuple[1])
print(type(my_tuple))

# You can count the ammount of instances of a tuple:
print(my_tuple.count('strings'))
print(my_tuple.index(4.5))

#iterate over a loop

for x in my_tuple:
    print(x)
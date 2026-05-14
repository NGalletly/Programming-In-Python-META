list1 = [1,2,3,4,5]
list2 = ['A', 'B', 'C']
list3 = ["hello", 1 , True, 40.22]

print(list3)

#Inserting into lists, needs to specify index and what to slot in. 
list3.insert(len(list3), 5)

print(list3, sep = " ")

# Append to add to end of list

list3.append(21)

print(list3, sep = " ")

# Can extend the list and add multiple values to the end
list3.extend(["a", "e", "i", "o", "u"])

print(list3, sep = " ")

#Pop to remove item, but you need to specify index
# list3[1] = 1
list3.pop(1)

print(list3, sep = " ")

# Del keyword to specify the index to remove
#list3[2] = 40.22
del list3[2]

print(list3, sep= " ")

#iteration
for x in list3:
    print(x)



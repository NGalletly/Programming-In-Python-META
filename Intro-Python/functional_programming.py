coffees = [ "americano", "long black", "cappucino", "latte"]
sorted_coffees= sorted(coffees)
# print(sorted_coffees)

def reverse(str):
    return str[::-1]

reversed_coffees_map = map(reverse, coffees)
reversed_coffees_list = []

for x in reversed_coffees_map:
    reversed_coffees_list.append(x)

# print(reversed_coffees_list)

# Pure function
numbers = [1,2,3]
def add_to_list(lst,item):
    clone = lst.copy()
    clone.append(item)
    return clone

print(add_to_list(numbers,4))


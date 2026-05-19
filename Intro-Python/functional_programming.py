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

# print(add_to_list(numbers,4))

# Recursion

def example(obj):
    #code
    return example(obj)


# Without recursion
def find_factorial_by_looping(n):
    if n <0:
        return 0
    else:
        factorial = 1
        for i in range(1, n+1):
            factorial = factorial *i
        return factorial
    
# With recursion
def find_factorial_recursive(n):
    if n ==1:
        return 1
    else:
        return n* find_factorial_recursive(n-1)





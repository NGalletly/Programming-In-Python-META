#kwargs = key word arguements

def sum_of(a,b):
    return a + b

# This doesnt work because third parameter is passed 
# print(sum_of(4,5,6))

#You can use *args
def sum_of(*args):
    sum = 0
    for x in args:
        sum += x
    return sum

print(sum_of(4,5,6))
print(sum_of(4,5,6,12,4,2,3,3))
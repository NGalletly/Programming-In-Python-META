# file = open('test.txt', mode = 'r')

# data = file.readline()
# print(data)

# file.close()

with open('test.txt', mode = 'r') as file:
    print(file.readline())

file.close()
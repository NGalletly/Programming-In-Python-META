name = "john"
if name == 'john':
    print(name)

    print('hello'); print('world')

def say_howdy():
    print('howdy')

print(say_howdy())

'''
multi line ignore not in green?
'''

# Ignore

# muti
# line 
# ignore

#Direct formatting
a=10
b=5
ans = a+b
print("Adding the value of {} and {} will equal {}".format(a,b,ans))


#Output formatting
print("I like {0} more than {1}".format("oranges", "grapes"))
print("I like {1} more than {0}".format("oranges", "grapes"))

#Input

name = input()
print("Hello", name, sep=(", "))
print("Hello" + ' ' + name)

a = input()
b = input()
ans = int(a)+int(b)

print(ans)
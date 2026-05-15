# def divide_by(a,b): 
#     return a / b

# try:
#     ans = divide_by(40,0)
# except Exception as e:
#     print("Something went wrong!", e)
#     print(e.__class__)

# try:
#     ans = divide_by(40,0)
# except ZeroDivisionError as e:
#     print(e, ", cannot divide by 0.")
#     print(e.__class__)

# print(divide_by(40,0))

items = [1,2,3,4,5]

try:
    item = items[6]
    print(item)
except Exception as e:  
    print("Error:", e , ". Please check the index range of list before assigning.")


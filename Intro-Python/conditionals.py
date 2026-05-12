bill =  105

discount1 = bill * .9
discount2 = bill * .85

if bill<=0:
    print("invalid bill!")
elif bill>200:
    print(f"bill is {str(bill)}, which is over 200 so you will receive a 15% discount.\
 After discount you will be charged {str(discount2)} which is a saving of {str(bill-discount2)}")
elif bill>100:
    print(f"bill is {str(bill)}, which is over 100 so you will receive a 10% discount.\
 After discount you will be charged {str(discount1)} which is a saving of {str(bill-discount1)}")
else:
    print(f"bill is {str(bill)}, which is under 100")

# MATCH statement

https_status = 200

match https_status:
    case 200 | 201:
        print("Success!")
    case 400:
        print("Not Found!")
    case 500 | 501:
        print("Server Error!")
    case _:
        print("Unknown status!")

 # FOR LOOPS

favourites = ["cake", "ice cream", "apple pie"]

for i in range(10):
	print('Looping...' , i)

for item in favourites:
    print("I like this desert", item)

count = 0
while count  < len(favourites):
		print("while I like this desert ", favourites[count])
		count += 1
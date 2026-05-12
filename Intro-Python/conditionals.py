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
bill = 0.1

if bill<=0:
    print("invalid bill!")
elif bill>100:
    print(f"bill is {str(bill)}, which is over 100.")
else:
    print(f"bill is {str(bill)}, which is under 100")
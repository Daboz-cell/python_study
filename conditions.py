a=20
b=50

if a>b:
    print("a is greater than b")
else:
    print("b is greater than a")

marks=input('Enter mark:')
marks=int(marks)
if marks>=50:
    print("Pass")
else:
    print("Fail")
password=input("Enter password: ")
correct_password="Dog"
if password==correct_password:
    print("Access granted")
else:
    print("Access denied")
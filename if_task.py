#Take three inputs from a user, separately. Print the largest of the numbers.
   # Hint: Determine what type of data is taken in as input.
a=input("Enter 1st Number:")
a=int(a)
b=input("Enter 2nd Number:")
b=int(b)
c=input("Enter 3rd Number:")
c=int(c)

if a>b and a>c :
    print(f"{a} is the largest number")
elif b>a and b>c :
    print(f"{b} is the largest number")
else:
    print(f"{c} is the largest number")

#Take four inputs from a user, separately. Print the largest of the numbers.
a=input("Enter 1st Number:")
a=int(a)
b=input("Enter 2nd Number:")
b=int(b)
c=input("Enter 3rd Number:")
c=int(c)
d=input("Enter 4th Number:")
d=int(d)


if a>b and a>c and a>d:
    print(f"{a} is the largest number")
elif b>a and b>c and b>d:
    print(f"{b} is the largest number")
elif c>a and c>b and c>d:
    print(f"{c} is the largest number")
else:
    print(f"{d} is the largest number")

#Take as input from a user the temperature if the temperature is above 30°C display “The temperature is too high”,if the temperature is above 15 display “Normal temperature” otherwise display “Cold temperature”
temp=input("User's temperature: ")
temp=float(temp)

if temp>30:
    print("The temperature is too high")
elif temp>15:
    print("Normal temperature")
else:
    print("Cold temperature")

#Write a Python program that checks if a variable x is between 10 and 20 (inclusive)
#and if another variable y is greater than 100. If both conditions are true, print "Conditions met", otherwise print "Conditions not met"

x=input("Enter Value of X: ")
x=int(x)
y=input("Enter value of Y:")
y=int(y)

if x>=10 and x<=20 and y>100:
    print("Conditions met")
else:
    print("Conditions not met")

#Write a Python program that checks if a variable password is equal to the string "secret123". If it is, print "Access   granted", otherwise print "Access denied"
password=input("Enter password: ")
correct_password="secret123"
if password==correct_password:
    print("Access granted")
else:
    print("Access denied")




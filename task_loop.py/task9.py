#Write a program called stars. It should prompt the user for a number, and it should print the number of stars till the number entered.
#Example If rows is 5, it should print the following:
#*
#**
#***
#****
#*****.....
number=int(input("Enter number of rows: "))
for i in range(1,number+1):
    print('*' *i)
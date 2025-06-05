#5 Implement a program that takes 3 users  inputs from the terminal or the Browser, and stores them in three variables. Return the largest of the three. Do this without using the the inbuilt max () function!
#The goal of this exercise is to think about some internals that programs normally take care of for us. 
a=input('Enter a value: ')
a=int(a)
b=input('Enter a value: ')
b=int(b)
c=input('Enter a value: ')
c=int(c)
if a or b or c==(int):
    if a>b and a>c:
        print(a)
        if b>a and b>c:
            print(b)
        else:
            print(c)      
else:
    print('Enter a number value')
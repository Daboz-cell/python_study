#Write a program that takes input of 2 values and adds them. The program should only accept numbers and floats only or otherwise display an error “invalid character entered” and take the user to re-enter the inputs .

while True:
    try:
        value1=input('Enter first value: ')
        value1=float(value1) or int(value1)
        value2=input('Enter second value: ')
        value2=float(value2) or int(value2)
        sum=value1+value2
        print(f'sum of the two numbers is: {sum}')
        break
    except:
        print('Invalid character entered try again')
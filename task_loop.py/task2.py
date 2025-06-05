#2. Prompt the user for a number either on a form input or the terminal. Depending on whether the number is even or odd, display  either “odd” or “even” to the user.
#Hint: how does an even / odd number react differently when divided by 2?

number=input("Enter a number: ")
number=int(number)

if number%2==0:
    print("Even number")
    if number%4==0:
        print("divisible by 4") 

else:
    print("odd number")
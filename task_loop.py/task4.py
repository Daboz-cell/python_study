#4 Write a program which accepts email as form input or from terminal. Validate the email by checking if it's a valid email. 
#Hint: Check if it contains an “@” symbol and “.” symbol.
email=input('Enter email: ')
#if "@" in email:
#    if "." in email:
        #print('Valid email')
#else:
    #print('Invalid email')


if email.find("@")==-1 and email.find(".")==-1:
   print('Invalid email')
else:
    print('Valid email')
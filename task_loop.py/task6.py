#6 Write a program that lets the user input a password. Give them only 4 attempts to check the passwords entered against “admin@123”. If the password is correct access is granted. After you show them a message , the account is blocked.
attempts=4
correct_password='admin@123'

for i in range(1,attempts+1):
    password=input('Enter password: ')
    if password==correct_password:
        print('Access granted')
        break
    else:
        remaining_attempts=attempts-i
        if remaining_attempts>0:
            print(f'Acces denied, You have {remaining_attempts} attempts left')
        else:
            print('Account blocked')
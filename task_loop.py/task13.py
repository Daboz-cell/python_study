# Write a program that takes the email and password as input from a user and checks if they are equal to “admin@mail.com” and password is “Admin@123” , 
# if so then print  “Login is Successful” and if not print “Invalid username or password”. 
# ONLY accept 3 tries after which it notifies you that you have been blocked.
email = 'admin@mail.com'
password = 'Admin@123'
attempts = 3

for i in range(attempts):
    user_email = input("Enter email: ")
    user_pass = input("Enter password: ")

    if user_email == email and user_pass == password:
        print("Login is Successful")
        break
    else:
        remaining_attempts = attempts-(i+1)
        if remaining_attempts>0:
            print("Invalid username or password")
            print(f"You have {remaining_attempts} attempt(s) left")
        else:
            print("You have been blocked")
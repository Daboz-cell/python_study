
correct_pin= 2079
attemps=3

for i in range(1,attemps+1):
    pin=input('Enter pin: ')
    pin=int(pin)
    if pin==correct_pin:
        print("Correct pin")
        break
    else:
        remaining_attempts=attemps-i
        if remaining_attempts>0:
            print(f'You have {remaining_attempts} attempts left ')
        else:
            print("You have run out of attempts")
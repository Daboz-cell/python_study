number=4
attemps=3

for i in range(1,attemps+1):
    guess=input('Guess the number: ')
    guess=int(guess)
    if guess==number:
        print('You guessed it right')
        break
    else:
        remaining_attempts=attemps-i
        if remaining_attempts>0:
            print(f'You have {remaining_attempts} attempts left')
        else:
            print('You have run out of attempts')
#Write a program that takes the date of birth of a person and the program outputs the age in terms of years,months,days TODAY.
from datetime import datetime
x=datetime.now()

current_month=x.month
current_year=x.year
current_day=x.day
dob=input('Enter your date of birth in the format dd/mm/yy: ')
dob=dob.split('/')
years=current_year-int(dob[2])
months=current_month-int(dob[1])
days=current_day-int(dob[0])

if months<0:
    years=years-1
    months=months+12
    if days<0:
        months=months-1
        days=days+30

print(f'you have {years} years {months} months {days} days')

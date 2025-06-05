fruits= ['Apple','Banana','Oranges','Melon']
for i in fruits:
    print(i)
#display odd numbers from 100 to 200
for i in range(100,200):
    if  i%2==0:
        print(i)

#store even numbers from 100 to 200
even_numbers=[]
numbers=list(range(100,201))

for num in numbers:
    if num%2==0:
        even_numbers.append(num)

print(even_numbers)

#store odd numbers from 100 to 200
odd_numbers=[]
numbers=list(range(100,200))

for num in numbers:
    if num%2!=0:
        odd_numbers.append(num)

print(odd_numbers)


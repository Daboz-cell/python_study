#Write a program that calculates the total stock in a company from the array/list below if we know that the stock is the last digit in every array/list.

prods = [['omo','30kshs','300'], ['milk','50kshs','200'],['bread','45kshs','359'], ['coffee','5kshs','79']]

#NB: ONCE YOU COPY AND PASTE THE LIST ABOVE,REWRITE THE SINGLE QUOTES AS THE ABOVE LIST WILL GIVE YOU AN ERROR.

total=0
for i in prods:
    i=list(i)
    i[2]=int(i[2])
    total=total+i[2]

print(total)
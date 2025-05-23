fruits=['Apple','Mango',[10,20,['a','e','i'],30],'Oranges','grapes']
print(type(fruits))
print(fruits[1])

print(fruits[2][2][0])

fruits[0]='Lemon'
print(fruits)


Week=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
print(Week[2])

Week.append(1000)
#Week.clear()
x=Week.copy()
#Week.remove('Sunday')
print(Week.count('Sunday'))
print(Week)
Week.pop(1)
Week.reverse()
y=[ 10, 20, 30 ,40]


numbers=[5,2,3,7,8,6]
numbers.sort(reverse=True)
print(numbers)
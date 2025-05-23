numbers={10,20,30,40,50}
print(type(numbers))
print(numbers)

#
x=["Kevin","Alex","Pauline","Brian","Kevin","Alex"]
x=set(x)
x=list(x)
print(x)

numbers.add(60)
print(numbers)

days = {"monday","tuesday","wednesday","thursday", "friday","saturday","sunday","sunday","sunday","sunday"}
print(days)

#Remove friday and sunday from the set using methods.
days.remove("friday")
days.remove("sunday")
print(days)
#Add them back to the set
days.add("friday")
days.add("sunday")
print(days)

first_name=" JOHn ."
first_name=first_name.lower()
first_name=first_name.replace('.','')
first_name=first_name.strip()
print(first_name)

#Question 2
sentence_one="The Dog Breed is German Shepherd"
sentence_two="Defeats for the Clinton forces, this was her momment of triumph"
print(sentence_one[8:24])
print(sentence_two[16:30])
#Question 3
sentence="The lazy dog; ran so fast; it hit the wall."
sentence=sentence.split(';')
print(sentence)
print(len(sentence))
#Question 4
first_name=" Joh.n"
first_name=first_name.replace('.','')
first_name=first_name.strip()
print(first_name)
last_name=" Do,e"
last_name=last_name.replace(',','')
last_name=last_name.strip()
print(last_name)
full_name=first_name+' '+last_name
print(full_name)
#Question 5
r='["E","W","C"]'
r=r.replace('[','')
r=r.replace('"' ,'')
r=r.replace(',','')
r=r.replace(']','')
print(r)











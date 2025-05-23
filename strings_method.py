
# Question 1
text=" learn python "
text_strip=text.strip()
print(text_strip)
text_title=text_strip.title()
print(text_title)

#Question 2
text2="hello"
print(text2[::-1])

#Question 3
text3=" learn python "
text_rep=text3.replace(' ','_')
print(text_rep)

#Question 4
text4=" learn python "


print(text4[10:13])

#2
#step 1
sentence=input("Enter a sentence: ")

#step 2
sentence_splitted=sentence.split(' ')
print(sentence_splitted)
print(len(sentence_splitted))
 
 #step 3
capitilized_sentence=sentence.title()
print(capitilized_sentence)

#step 4
reversed_sentence=capitilized_sentence[::-1]
print(reversed_sentence)

#3
text_3="  BAD habits are hard to break! "
text_3=text_3.replace('BAD','good')
text_3=text_3.strip()
print(text_3)

#4
email="  John.Doe@GMAIL.com "
email=email.strip()
email=email.lower()
print(email)



#5
first="john"
first=first.capitalize()
last="Doe"
last=last.capitalize()
hobby=" Reading Books "
hobby=hobby.strip()

sentence= f" My Name is 'first' + 'last' and I love 'hobby' "


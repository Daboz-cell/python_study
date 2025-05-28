# Write a program that:
# = > Takes the user's credit score and annual income as input.
# =>If the credit score is above 700, check if the income is above 50,000:
# =>If both conditions are met, print "Loan approved."
# =>If only the credit score is high, print "Income requirement not met."
# =>If the credit score is below 700, print "Credit score too low."

credit_score=input("Enter credit score: ")
credit_score=int(credit_score)
annual_income=input("Enter annual_income: ")
annual_income=int(annual_income)

if credit_score>700:
    if annual_income>50000:
        print("Loan approved")
    else:
        print("Income requirement not met")
else:
    print("Credit score too low")      

#Write a Python program that checks if a variable student_score is greater than 90. If true, check if the attendance is greater than 80. If both conditions are true, print "Excellent student", otherwise print "Good score, but attendance needs improvement"
student_score=input("Enter student score: ")
student_score=int(student_score)
attendance=input("Enter attendance: ")
attendance=int(attendance)

if student_score>90:
    if attendance>80:
        print("Excellent student")
    else:
        print("Good score, but attendance needs improvement")
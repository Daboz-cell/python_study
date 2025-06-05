#7 Write that prompts the user to input student marks. The input should be between 0 and 100.Then output the correct grade: 
#A > 79 , B - 60 to 79, C  > 49 to 59, D - 40 to 49, E - less 40

student_marks=input('Enter student marks: ')
student_marks=int(student_marks)
if student_marks>=0 and student_marks<=100:
    if student_marks>79:
        print('A')
    elif student_marks>59:
        print('B')
    elif student_marks>49:
        print('C')
    elif student_marks>39:
        print('D')
    else:
        print('E')
else:
    print('The input should be between 0 and 100')
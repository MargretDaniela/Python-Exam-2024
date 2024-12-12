#Part (i)
age = int(input("Enter age:"))
if age >= 18:
    print("You are eligible") #Above and equal to 18 one is eligible

else:
    print("You arenot eligible")#Below 18 one isnot eligible

# #Part (ii)
def grade_students():
    marks = int(input("Enter the marks:")) #Am prompting the user to enter their marks
    if marks >= 90:
        print("Grade A")
    elif marks < 89 and marks > 80:
        print("Grade B")
    elif marks < 79 and marks > 70:
        print("Grade C")
    elif marks < 69 and marks > 60:
        print("Grade D")
    else:
        print('Grade F')
grade_students()
# # Part (iii)
def grade_students():
    marks = 85
    if marks >= 90:
        print("Grade A")
    elif marks < 89 and marks > 80:
        print("Grade B")
    elif marks < 79 and marks > 70:
        print("Grade C")
    elif marks < 69 and marks > 60:
        print("Grade D")
    else:
        print('Grade F')
grade_students() #Testing the funtion with 85
# Part (iv)
def grade_students(marks):
    try:
        if marks is 85:
            marks = input("Enter the marks please: ")
            marks = int(marks) 
        if isinstance(marks, int): #Making the program know that the valid inputs are intergers
            if marks >= 90:
                print(' Grade A')
            elif marks >= 80 and marks < 89:
                print("Grade B")
            elif marks >= 70 and marks < 79:
                print("Grade C")
            elif marks >= 60 and marks < 69:
                print('Grade  D')
            else:
                print(' Grade F')
        else:
            return "invalid input" #Making the program know that ifnot intergers or floats thats an invalid input.
    except ValueError:
        return "valid input"  
print(grade_students(marks=85))#Thats the valid input 
print(grade_students(marks="Derrick")) #This is the invalid input 

#Part (v)

def grade_students():
    marks = 78
    if marks >= 90:
        print(" Grade A Excellent")#Returns the grade and its corresponding message
    elif marks < 89 and marks > 80:
        print("Grade B Excellent")#Returns the grade and its corresponding message
    elif marks < 79 and marks > 70:
        print(" Grade C Good")#Returns the grade and its corresponding message
    elif marks < 69 and marks > 60:
        print("Grade E Satisfactory")#Returns the grade and its corresponding message
    else:
        print("Grade F Needs improvement ")#Returns the grade and its corresponding message
grade_students()#Calling the function
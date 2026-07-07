'''Write a Python program that defines a function calculate_grade(marks).

The function should:

Accept marks (0–100) as a parameter.
Return the grade according to the following criteria:
90 and above → A+
75–89 → A
60–74 → B
40–59 → C
Below 40 → Fail
The main program should:

Accept marks of 5 students.
Call the function for each student.
Display the marks and corresponding grade.'''

#Ddefine a function to calculate grade based on marks
def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 75:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "Fail"
    
#input marks for 5 students
marks_list = []
for i in range(5):
    marks = float(input(f"Enter marks for student {i+1} (0-100): "))
    marks_list.append(marks)

#display marks and corresponding grade for each student
for i in range(5):
    grade = calculate_grade(marks_list[i])
    print(f"Student {i+1}: Marks = {marks_list[i]}, Grade = {grade}")


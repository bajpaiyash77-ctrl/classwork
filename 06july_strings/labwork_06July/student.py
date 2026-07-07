''''Create a dictionary to store the marks of 5 students in dictionary. The key of the dictionary is the name of the student and the value is the marks of the student.'''
'''display all students with marks'''
'''add a new student and marks to the dictionary'''
'''update the marks of a student in the dictionary'''
'''delete a student from the dictionary'''
'''display the student with highest marks'''

#Creating a dictionary to store the marks of 5 students
student_marks = {}

#Adding 5 students and their marks to the dictionary
for i in range(5):
    name = input("Enter the name of student: ",)
    marks = int(input("Enter the marks of student: "))
    student_marks[name] = marks 

#Displaying all students with marks
print("The students with their marks are: ")
for name, marks in student_marks.items():
    print(name, ":", marks)

#Adding a new student and marks to the dictionary
new_name = input("Enter the name of new student: ")
new_marks = int(input("Enter the marks of new student: "))
student_marks[new_name] = new_marks

#Updating the marks of a student in the dictionary
update_name = input("Enter the name of student whose marks you want to update: ")
update_marks = int(input("Enter the new marks of student: "))
if update_name in student_marks:
    student_marks[update_name] = update_marks
else:
    print("Student not found in the dictionary.")

#Deleting a student from the dictionary
delete_name = input("Enter the name of student you want to delete: ")
if delete_name in student_marks:
    del student_marks[delete_name]
else:
    print("Student not found in the dictionary.")

#Displaying the student with highest marks
highest_marks = max(student_marks.values())
for name, marks in student_marks.items():
    if marks == highest_marks:
        print("The student with highest marks is: ", name, "with marks: ", marks)
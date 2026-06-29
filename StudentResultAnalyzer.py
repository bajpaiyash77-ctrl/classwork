'''student result analyzer'''
#input marks for n students
n = int(input("Enter the number of students: "))
#marks should be out of 100 for each student
marks = []
for i in range(n):
    mark = int(input(f"Enter marks for student {i + 1} (out of 100): "))
    while mark < 0 or mark > 100:
        print("Invalid marks. Please enter marks between 0 and 100.")
        mark = int(input(f"Enter marks for student {i + 1} (out of 100): "))
    marks.append(mark)

#hieghest marks and lowest marks and average marks and number of students with marks more than or equal to 75 and number of students with marks more than 40
highest_marks = max(marks)
lowest_marks = min(marks)
average_marks = sum(marks) / n if n > 0 else 0
count_above_75 = sum(1 for mark in marks if mark >= 75)
count_above_40 = sum(1 for mark in marks if mark >= 40)

print(f"Highest marks: {highest_marks}")
print(f"Lowest marks: {lowest_marks}")
print(f"Average marks: {average_marks:.2f}")
print(f"Number of students with marks >= 40: {count_above_40}")
print(f"Number of students with marks >= 75: {count_above_75}")



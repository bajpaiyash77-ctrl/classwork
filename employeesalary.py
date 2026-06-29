''''employee salary statistics'''
#input n employee salaries
n = int(input("Enter the number of employees: "))
#determine the highest and lowest salary and average salary of the employees and number of employtees with salary more than 50000
highest_salary = 0
lowest_salary = float('inf')
total_salary = 0
count_high = 0

for _ in range(n):
    salary = float(input("Enter employee salary: "))
    total_salary += salary

    if salary > highest_salary:
        highest_salary = salary

    if salary < lowest_salary:
        lowest_salary = salary

    if salary > 50000:
        count_high += 1

average_salary = total_salary / n if n > 0 else 0

print(f"Highest salary: {highest_salary}")
print(f"Lowest salary: {lowest_salary}")
print(f"Average salary: {average_salary:.2f}")
print(f"Number of employees with salary more than 50000: {count_high}")
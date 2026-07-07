# Define a function to find the maximum value in a list
def find_max(numbers):
    return max(numbers)

# Define a function to find the minimum value in a list
def find_min(numbers):
    return min(numbers)

# Define a function to find the average value of a list
def find_average(numbers):
    return sum(numbers) / len(numbers)

# Input a list of 10 integers from the user
numbers = []
for i in range(10):
    num = int(input(f"Enter integer {i+1}: "))
    numbers.append(num)

# Call the functions and display the results
max_value = find_max(numbers)
min_value = find_min(numbers)
average_value = find_average(numbers)
print(f"Maximum value: {max_value}")
print(f"Minimum value: {min_value}")
print(f"Average value: {average_value}")
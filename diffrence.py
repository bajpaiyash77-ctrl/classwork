'''calculate the difference between two numbers'''
#input two numbers
num1 = float(input("Enter the first number: ")) 
num2 = float(input("Enter the second number: "))
#validation of inputs
if num1 < 0 or num2 < 0:
    exit(ValueError("Both numbers must be non-negative."))
#display inputs
print("The first number is:", num1)
print("The second number is:", num2)
#calculate the difference
difference = num1 - num2
#display the result
print("The difference between the two numbers is:", difference)
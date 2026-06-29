'''Number Guessing Game'''
#input number
number = int(input("Enter a number "))
#Secret number to guess
secret_number = 37
#validation of number
#while number is not equal to secret_number, keep asking for a new number
while number != secret_number:
    if number < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    number = int(input("Enter a number "))
print("Correct.")
'''Write a function check_password(password) that checks whether a password is strong.

A password is considered Strong if:

It contains at least 8 characters.
It contains at least one uppercase letter.
It contains at least one lowercase letter.
It contains at least one digit.
The function should return:

"Strong Password" or
"Weak Password"
The main program should accept a password from the user and display the result.'''

# Define a function to check the strength of a password
def check_password(password):
    # Check if the password has at least 8 characters
    if len(password) < 8:
        return "Weak Password"
    
    # Check for at least one uppercase letter
    if not any(char.isupper() for char in password):
        return "Weak Password"
    
    # Check for at least one lowercase letter
    if not any(char.islower() for char in password):
        return "Weak Password"
    
    # Check for at least one digit
    if not any(char.isdigit() for char in password):
        return "Weak Password"
    
    return "Strong Password"

# Main program to accept a password from the user and display the result
password = input("Enter a password to check its strength: ")
result = check_password(password)
print(result)

'''Password Strenghth Checker'''
#input password
password = input("Enter a password ")
#validation of password
while len(password) < 8:
    print("Password is too short")
    password = input("Enter a password ")
print("Password ACCEPTED")
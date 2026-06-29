'''Login System'''
username = input("Enter username: ")
password = input("Enter password: ")
# Correct credentials
correct_username = "admin"
correct_password = "python123"

# Validation of credentials and only 3 attempts allowed
attempts = 0
while attempts < 3:
    if username == correct_username and password == correct_password:
        print("Login successful!")
        break
    else:
        attempts += 1
        print(f"Incorrect username or password. Attempts left: {3 - attempts}")
        if attempts < 3:
            username = input("Enter username: ")
            password = input("Enter password: ")

if attempts == 3:
    print("Account Locked")
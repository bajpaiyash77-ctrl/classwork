'''ATM PIN Verification System'''
#input pin
pin = input("Enter your 4-digit ATM PIN: ")
#Correct  pin
correct_pin = "4589"
#while loop for pin verification
while pin != correct_pin:
    print("Incorrect PIN ")
    pin = input("Enter your 4-digit ATM PIN: ")

print("ACCESS GRANTED.")
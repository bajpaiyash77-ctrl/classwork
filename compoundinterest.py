'''compound interest'''
#input principal, rate, time
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in %): "))
time = int(input("Enter the time in years: "))
#validation of inputs
if principal < 0 or rate < 0 or time < 0:
    exit(ValueError("Principal, rate, and time must be non-negative."))
#display inputs
print("The principal amount is:", principal)
print("The annual interest rate is:", rate) 
print("The time in years is:", time)
#calculate compound interest
compound_interest = principal * (1 + rate / 100) ** time
#display the result
print("The compound interest after", time, "years is:", compound_interest)
#define a function to calculate simple interest
def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

#main function to take user input and call the calculate_simple_interest function
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = int(input("Enter the time in years: "))
print("The simple interest is:", calculate_simple_interest(principal, rate, time))
def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100


def main():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest: "))
    time = int(input("Enter the time in years: "))
    interest = calculate_simple_interest(principal, rate, time)
    print("The simple interest is:", interest)


if __name__ == "__main__":
    main()
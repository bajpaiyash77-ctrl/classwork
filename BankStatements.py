'''Bank transaction summary'''

balance = 0.0
deposits = 0.0
withdrawals = 0.0

print("Enter bank transactions. Enter 0 to exit.")
print("Use positive values for deposits and negative values for withdrawals.")

while True:
    amount = float(input("Enter amount: "))

    if amount == 0:
        break

    balance += amount

    if amount > 0:
        deposits += amount
    else:
        withdrawals += abs(amount)

    print(f"Current balance: {balance:.2f}")

print("\nTransaction summary")
print(f"Total deposits: {deposits:.2f}")
print(f"Total withdrawals: {withdrawals:.2f}")
print(f"Final balance: {balance:.2f}")

'''Create a simple Bank Account class that allows users to deposit and withdraw money. '''
#creating Class
class BankAccount:
    #Defining the constructor
    def __init__(self):
        self.account_number = ""
        self.customer_name = ""
        self.balance = 0

    def accept_details(self):
        self.account_number = input("Enter Account Number : ")
        self.customer_name = input("Enter Customer Name : ")
        self.balance = float(input("Enter Initial Balance : "))

    def deposit(self, amount):
        self.balance += amount
        print("Deposit Successful.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal Successful.")
        else:
            print("Insufficient Balance.")

    def display_balance(self):
        print("\n------ Account Details ------")
        print("Account Number :", self.account_number)
        print("Customer Name :", self.customer_name)
        print("Current Balance:", self.balance)


# Creating object and performing operations
acc = BankAccount()
acc.accept_details()

deposit_amount = float(input("Enter Deposit Amount : "))
withdrawal_amount = float(input("Enter Withdrawal Amount : "))

acc.deposit(deposit_amount)
acc.withdraw(withdrawal_amount)
acc.display_balance()
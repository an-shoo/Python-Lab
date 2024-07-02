class SavingsAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        print(f"Withdrew {amount}. New balance is {self.balance}.")

    def display_balance(self):
        print(f"Account balance: {self.balance}")

try:
    account = SavingsAccount("1234567890", "John Doe", 1000)
    account.deposit(500)
    account.withdraw(200)
    account.display_balance()
except ValueError as e:
    print(e)

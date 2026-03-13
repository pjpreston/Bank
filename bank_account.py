class BankAccount:
    def __init__(self, customer, opening_balance=0):
        if not customer:
            raise ValueError("Customer is required.")
        if opening_balance < 0:
            raise ValueError("Opening balance cannot be negative.")

        self.customer = customer
        self.balance = opening_balance

    def add_cash(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")

        self.balance += amount
        return self.balance

    def withdraw_cash(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")

        self.balance -= amount
        return self.balance

from exceptions import InsufficientBalanceError, TransactionLimitError

class BankAccount:
    TRANSACTION_LIMIT = 50000

    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.TRANSACTION_LIMIT:
            raise TransactionLimitError(amount)

        if amount > self.balance:
            raise InsufficientBalanceError(self.balance, amount)

        self.balance -= amount
        return f"Withdrawal successful. Remaining balance: {self.balance}"

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")

        self.balance += amount
        return f"Deposit successful. Updated balance: {self.balance}"

    def calculate_interest(self, rate, time):
        return (self.balance * rate) / time
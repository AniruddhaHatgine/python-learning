class InsufficientBalanceError(Exception):
    def __init__(self, balance, amount):
        super().__init__(f"\n Insufficient balance. Available: {balance}, Requested: {amount}")

class InvalidAccountError(Exception):
    def __init__(self, acc_no):
        super().__init__(f"\n Account {acc_no} is invalid or does not exist.")

class TransactionLimitError(Exception):
    def __init__(self, amount):
        super().__init__(f"\n Transaction limit exceeded for amount: {amount}")


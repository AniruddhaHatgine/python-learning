# --- Custom Exception Classes ---

class InsufficientBalanceError(Exception):
    def __init__(self, balance, amount):
        super().__init__(f"\n Insufficient balance. Available: {balance}, Requested: {amount}")

class InvalidAccountError(Exception):
    def __init__(self, acc_no):
        super().__init__(f"\n Account {acc_no} is invalid or does not exist.")

class TransactionLimitError(Exception):
    def __init__(self, amount):
        super().__init__(f"\n Transaction limit exceeded for amount: {amount}")


# --- Bank Account Class ---

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
        return f"\n Withdrawal successful. Remaining balance: {self.balance}"

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("\n Deposit amount must be positive")  # Built-in exception
        
        self.balance += amount
        return f"\n Deposit successful. Updated balance: {self.balance}"

    def calculate_interest(self, rate, time):
        # Demonstrating ZeroDivisionError & TypeError
        return (self.balance * rate) / time


# --- Banking Service Layer ---

class BankingService:
    def __init__(self):
        self.accounts = {
            101: BankAccount(101, 10000),
            102: BankAccount(102, 5000)
        }

    def get_account(self, acc_no):
        if acc_no not in self.accounts:
            raise InvalidAccountError(acc_no)
        return self.accounts[acc_no]

    def transfer(self, from_acc, to_acc, amount):
        sender = self.get_account(from_acc)
        receiver = self.get_account(to_acc)

        sender.withdraw(amount)
        receiver.deposit(amount)

        return "\n Transfer successful"


# --- Main Execution (Simulation) ---

service = BankingService()

try:
    print("\n --- Banking Transaction Started --- \n")

    acc = service.get_account(101)
    print("Balance Fetched : ", acc.balance)

    # Note: Uncomment one of these at a time to test different exception scenarios:

    # 1. Valid withdrawal
    # print(acc.withdraw(2000))

    # 2. Invalid deposit (built-in ValueError)
    # print(acc.deposit(-500))

    # 3. Transfer with insufficient balance (custom exception)
    # print(service.transfer(101, 102, 20000))

    # 4. Invalid account
    # print(service.get_account(999))

    # 5. Interest calculation error (ZeroDivisionError)
    # print(acc.calculate_interest(5, 0))

except InsufficientBalanceError as e:
    print("\n Custom Error:", e)

except InvalidAccountError as e:
    print("\n Custom Error:", e)

except TransactionLimitError as e:
    print("\n Custom Error:", e)

except ValueError as e:  # Built-in
    print("\n ValueError:", e)

except ZeroDivisionError as e:  # Built-in
    print("\n ZeroDivisionError:", e)

except TypeError as e:  # Built-in
    print("\n TypeError:", e)

except Exception as e:
    print("\n General Exception:", e)

else:
    print("\n Message Sent to Account Holder")

finally:
    print("\n Transaction Logged... \n \n")
#Custom Excpetion

class InsuficientBalanceError(Exception):
    def __init__(self,balance,amount):
        self.balance = balance
        self.amount = amount
        super().__init__("Balalnce is not sufficient")

class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def withdraw(self,amount):
        try:
            if amount > self.balance:
                raise InsuficientBalanceError(self.balance,amount)

            self.balance -=amount
            print("Transaction Successful!")

        except InsuficientBalanceError as e:
            print("Custom Error:",e)

        finally:
            print("Tranasaction logged..")


account = BankAccount("Sandesh",5000)
account.withdraw(7000)
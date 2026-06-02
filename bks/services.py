from models import BankAccount
from exceptions import InvalidAccountError

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

        return "Transfer successful"
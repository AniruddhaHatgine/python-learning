from service import BankingService
from exceptions import (
    InsufficientBalanceError,
    InvalidAccountError,
    TransactionLimitError   
)   


def main():
    
    try:
        service = BankingService()

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

if __name__ == "__main__":
    main()
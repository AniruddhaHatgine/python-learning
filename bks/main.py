from services import BankingService
from exceptions import (
    InsufficientBalanceError,
    InvalidAccountError,
    TransactionLimitError
)

def main():
    service = BankingService()

    try:
        print("\n--- Banking Transaction Started ---")

        acc = service.get_account(101)

        print(acc.withdraw(2000))
        print(acc.deposit(-500))  # ValueError
        print(service.transfer(101, 102, 20000))  # Custom error
        print(service.get_account(999))  # Invalid account
        print(acc.calculate_interest(5, 0))  # ZeroDivisionError

    except InsufficientBalanceError as e:
        print("Custom Error:", e)

    except InvalidAccountError as e:
        print("Custom Error:", e)

    except TransactionLimitError as e:
        print("Custom Error:", e)

    except ValueError as e:
        print("Built-in ValueError:", e)

    except ZeroDivisionError as e:
        print("Built-in ZeroDivisionError:", e)

    except Exception as e:
        print("General Exception:", e)

    else:
        print("All transactions successful")

    finally:
        print("--- Transaction session ended ---")


if __name__ == "__main__":
    main()
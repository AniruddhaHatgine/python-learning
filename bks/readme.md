
# 🏦 Banking Service System (Python)

A modular Python project demonstrating 
real-world exception handling, 
clean architecture, and 
service-based design
using a banking use case.


## Features

Modular project structure (industry-style)
Custom exception handling
Built-in exception usage
Service layer abstraction
Clean separation of concerns
Real-world banking scenarios



## Project Structure

banking_app/
│
├── exceptions.py     # Custom exception classes
├── models.py         # Core business logic (BankAccount)
├── services.py       # Service layer (Banking operations)
├── main.py           # Entry point (execution)
└── __init__.py       # (optional) for package structure


## Architecture Overview

 Layer           | Responsibility                            
 --------------- | --------------------------------------------
 `models.py`     | Core domain logic (Account operations)    
 `services.py`   | Business workflows (transfer, validation) 
 `exceptions.py` | Domain-specific error handling           
 `main.py`       | Execution & orchestration                 



### 1. Create Project

mkdir banking_app
cd banking_app


### 2. Run Application


python main.py


##  Core Components

### BankAccount (models.py)

Handles:

* Withdraw
* Deposit
* Interest calculation

Example:

acc.withdraw(2000)
acc.deposit(500)


### BankingService (services.py)

Handles:

* Account lookup
* Money transfer

Example:

service.transfer(101, 102, 1000)


### 🔹 Custom Exceptions (exceptions.py)

 Exception                  | Purpose            |
 -------------------------- | ------------------ |
 `InsufficientBalanceError` | Not enough balance |
 `InvalidAccountError`      | Account not found  |
 `TransactionLimitError`    | Limit exceeded     |


## Exception Handling Covered

### Custom Exceptions

raise InsufficientBalanceError(balance, amount)


### Built-in Exceptions

* `ValueError` → Invalid input
* `ZeroDivisionError` → Invalid math
* `TypeError` → Wrong data type
* `Exception` → Fallback handler


## Execution Flow

1. Load accounts
2. Perform operations:

   * Withdraw
   * Deposit
   * Transfer
3. Handle errors using:

   * Multiple `except` blocks
   * `else` block (success case)
   * `finally` block (cleanup/logging)


## Sample Output


--- Banking Transaction Started ---
Withdrawal successful. Remaining balance: 8000
Built-in ValueError: Deposit amount must be positive
Custom Error: Insufficient balance...
--- Transaction session ended ---

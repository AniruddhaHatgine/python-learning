balance =  50000
withdaw_amount = 2000

if withdaw_amount <= balance:
    balance = balance - withdaw_amount
    print("Transaction Successful")
    print("Remaining Balance:",balance)
else:
    print("Insufficient Balance")    
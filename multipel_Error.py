def withdraw(amt):
    try:

        balance = 1000
        if amt > balance:
            raise Exception("Insufficient Balance")
        else:
            print("Tranasction Successful")


        a=int("a100")    #here only int means number should give but we gave letter a so it is showing built in error.

    except ValueError as e:
        print("ValueError:",e)     

    except TypeError as e:
        print("TypeError:",e)

    except Exception as e:
        print("Error:",e)          

withdraw(500)

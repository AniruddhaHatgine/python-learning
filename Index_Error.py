def withdraw(amt):
    try:
        balance = 1000
        if amt >= balance:
            raise Exception("insufficient balance")  #custom error handling
        else:
            print("Tranasction Successfu")

        a = int("100")   #type casting value error    

        list = [1,2,3]   #this will raise index error
        ls = list[5]

    except ValueError as e:   #will not trigger because there is no valueerror
        print("ValueError:",e)

    except IndexError as e:   #will trigger because at line 11 and 12 error is given
        print("IndexError:",e)

    except Exception as e:  #will not trigger cause not given
        print("Error:",e)

withdraw(500)                    
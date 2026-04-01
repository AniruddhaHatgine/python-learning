
def div():
    try:
        a= int(input("Enter a:"))
        b= int(input("Enter b:"))
        if b<=0:
            raise Exception("b can not be 0 or less than zero")
        c = a/b
        print("Div:",c)

    except Exception as e:
        print("Error:",e)

    finally:
        print("This is final")    

div()        
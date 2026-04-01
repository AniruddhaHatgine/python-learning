#error handlig
#sy

def div():
    try:
        a= int(input("Enter a:"))
        b= int(input("Enter b:"))
        c = a/b
        print("Div:",c)

    except Exception as e:
        print("Error:",e)

    finally:
        print("This is final")    

div()        
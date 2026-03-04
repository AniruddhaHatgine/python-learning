

def addition(a,b):
    print("addition")
    #addition
    return a+b

def substraction(x,y):
    print("Substration")
    #substraction
    print(x-y)

def multiplication(a,b): #(a,b) parameter and arguments
    print("multiplication")
    #multiplication
    print(a*b)

print("What you want to do? 1 for Addition 2 for Substration")
user_input = int(input("Enter Value:"))

if user_input==1 :
    a = 10
    b = 5
    c= addition(a,b)
    print(c)

elif user_input == 2 :
    c = 20
    d = 5
    d= substraction(c,d)
    print(d)

else:
    print("Wrong choice!")
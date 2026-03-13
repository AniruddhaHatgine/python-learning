###############################################
def addition(num1, num2):
    add = num1 + num2
    print("Addition : ",add)

def substraction(num1,num2):
    sub = num1 - num2
    print("Substration :", sub)
    
def multiplication(num1,num2):
    mult = num1 * num2
    print("Multiplication :", mult)
    
def division(num1,num2):
    div = num1 / num2
    print("Division :", div)
    
def user_input():
    a=int(input("Enter Number1:"))
    b=int(input("Enter Number2:"))
    return a,b
    
##################################################
# Program Execution starts here:
print("----------------------------")
print(" 1. Addition \n 2. Substraction \n 3.Multiplication \n 4. Division")
print("----------------------------")

user_input_option = input()
match user_input_option:
    case "1":
        a,b=user_input()
        addition(a,b)
    case "2":
        a,b=user_input()
        substraction()
    case "3":
        a,b=user_input()
        multiplication()
    case "4":
        a,b=user_input()
        division()
    case _:
        print("Invalid Choice..")
        
        
        
        
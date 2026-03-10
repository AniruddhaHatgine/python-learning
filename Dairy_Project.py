print("Which Milk? 1 for cow milk, 2 for buffalo milk")
user_input = int(input("Enter Value:"))

if user_input==1 :
    print("Cow Milk")
elif user_input==2 :
    print("Buffalo Milk")
else:
    print("Invalid Input")


print("How much Liter Milk")
Liters = int(input("Enter Value:"))
#if user_input > 0:
print("Accepted")

print("How much Fat Calculated in Milk")
user_input = int(input("Enter Value:"))
if user_input > 7:
    print("High Fat")
    amount = Liters * 50

if user_input == 7:
    print("Medium Fat")
    amount = Liters * 40
    
if user_input < 7:
    print("Low Fat")
    amount = Liters * 30
print(f"Total Amount is: {amount}")


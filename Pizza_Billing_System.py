pizza_name=input("Enter the name of the pizza: ")
pizza_size=input("Enter the size of the pizza (small, medium, large): ")
print("How much quantity of pizza")
quantity = int(input("Enter Value:"))
#if user_input > 0:
print("Accepted")
pizza_menu = {
    "Onion Pizza": 150,
    "Cheese Pizza": 200,
    "Veggie Pizza": 180,
    "Pepperoni Pizza": 250
}

if pizza_name in pizza_menu:
    price = pizza_menu[pizza_name]

    # quantity = int(input("Enter the quantity of pizzas: "))
    # quantity = max(1, quantity)  # Ensure quantity is at least 1
    
    total_cost = price * quantity
    print(f"Pizza Name: {pizza_name}")
    print(f"Pizza Size: {pizza_size}")
    print(f"Quantity: {quantity}")
    print(f"Total Cost: {total_cost}")

else:
    print("Sorry, we don't have that pizza on the menu.")   


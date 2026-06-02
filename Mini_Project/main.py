from services import add_expense, get_all_expenses, filter_by_category, total_expense

def menu():
    print("\n1. Add Expense")
    print("2. View All")
    print("3. Filter by Category")
    print("4. Total Expense")
    print("5. Exit")

while True:
    menu()
    choice = input("Enter choice: ")

    try:
        if choice == "1":
            amount = float(input("Amount: "))
            category = input("Category: ")
            note = input("Note: ")

            add_expense(amount, category, note)

        elif choice == "2":
            for exp in get_all_expenses():
                print(exp)

        elif choice == "3":
            category = input("Category: ")
            for exp in filter_by_category(category):
                print(exp)

        elif choice == "4":
            print("Total:", total_expense())

        elif choice == "5":
            break

        else:
            print("Invalid choice")

    except Exception as e:
        print("Error:", e)
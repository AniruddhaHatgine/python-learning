Buy=1000
Discount_Above=4000
Discount_Amount=3000

if Buy >= 4000:
    print("Discount applied")
    Bill_amount = Buy - Discount_Amount
    print(f"Discount Applied: {Discount_Amount}, Final Bill is: {Bill_amount}")
else:
    print("No Discount")
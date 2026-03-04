purchase=8000
discount=500
discount_abv_5k=1000
discount_abv_7k=1500
discount_abv_9k=2000

if purchase >= 3000:
    print("Discount applied..")
    if purchase >= 9000:
        Bill_amount = purchase - discount_abv_9k
        print(f" Rs.{discount_abv_9k} discount applied. Final Bill is {Bill_amount} ")
    elif purchase >= 7000:
        Bill_amount = purchase - discount_abv_7k
        print(f" Rs.{discount_abv_7k} discount applied. Final Bill is {Bill_amount} ")
    elif purchase >= 5000:
        Bill_amount = purchase - discount_abv_5k
        print(f" Rs.{discount_abv_5k} discount applied. Final Bill is {Bill_amount} ")
    else:  # for 3000 amt   
        Bill_amount=purchase - discount
        print(f"Rs.{discount} discount applied. Final Bill is {Bill_amount}")
else:
    print("No Discount")
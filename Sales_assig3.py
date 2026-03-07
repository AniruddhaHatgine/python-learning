monthly_sales=(250000,300000,280000,350000,40000,420000)
print("March Sales:",monthly_sales[2])
print("Feb Sales:",monthly_sales[1])
print("Jan Sales:",monthly_sales[0])

print("May Sales:",monthly_sales[4])
print("June Sales:",monthly_sales[5])

print("Total Months:", len(monthly_sales))

next_quarter=(450000,490000,500000)
full_year_sales=monthly_sales+next_quarter
print(full_year_sales)


bonus_month=(10000,)
print(bonus_month*3)

count = monthly_sales.count(300000)
print("Count of 300000 in sales:", count)

count=monthly_sales.count(9000000)
print("count of 9000000 in sales:",count)
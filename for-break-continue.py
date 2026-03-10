capacity=10

# for can in range(1,15):
#     if can <= 10:
#         print(can) 
#     else:
#         break
    
# print("outside looping")

list_milk_type=["C","B","G","B","G","C","C","G","B","G","G","B"]

for milk_type in list_milk_type:
    if milk_type=="G":
        # print("G skipped")
        continue
    else:
        print("collected")

  

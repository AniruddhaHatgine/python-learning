# students=[2,4,3,2,3,2]
# for student in students:
#     if student==1:
#         print("Trip Canceld")
#         break
# else:
#     print("Trip conformed")        



# menu=["Dosa","Idly","Vada","Pongal"]
# for menu_index, menu_name in enumerate(menu,start=3):       #enumerate is used to get index and value of list
#     print(f"number:{menu_index} name:{menu_name}")

#Zip 
student_name = ["Amit","Suhas","Nitin"]
student_roll = [20,22,25]

for name, rollno in zip(student_name,student_roll):
    print(f"Name is {name}  and Roll No is {rollno}")
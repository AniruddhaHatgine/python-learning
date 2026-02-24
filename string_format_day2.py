## Validation Methods
Owner_Name = "Aniruddha Hatgine"    # Database = Datatpe = String (plain text)
Car_Year = 2020                     # Database = Datatype = Integer
Car_Number = "MH12AB1234"           # Database = Datatype = String (alphanumeric)
Car_Chasis_Number = "12345"            # Database = Datatype = String (Emtyp Space) 
Car_Comany_Name = "HONDA"           # Database = Datatype = String (Uppercase)

# print("Is Owner Name has first letter Capital  :  ", Owner_Name.istitle())          # return True or False
# print("Is Car Year has first numbers only  :  ", Car_Year.is_integer())          # return True or False
# print("Is Car Number alphanumeric  :  ", Car_Number.isalnum())          # return True or False
# print("Is Car Chasis Value is empty space  :  ", Car_Chasis_Number.isspace()) 
# #print("Error: Please update chasis number..")         # return True or False
# print("Is Car Company Name is in Uppercase  :  ", Car_Comany_Name.isupper())          # return True or False

# print("Validating your car details : \n")
# if not Owner_Name.istitle():
#     print("Error: Owner Name is not valid..")
# elif not Car_Year.is_integer():                             # Else if -> python syntax is elif
#     print("Error: Car Year is not valid..")
# elif not Car_Number.isalnum():
#     print("Error: Car Number is not valid..")  
# elif Car_Chasis_Number.isspace():
#     print("Error: Please update chasis number..")
# elif not Car_Comany_Name.isupper():
#     print("Error: Car Company Name is not valid..")
# else:
#     print("Success : All data is valid..")

# print("\n Validation process is completed..")


#### Splitting and Joining String

car_number_with_dash = "MH12-AB-1234"

print("Car Details with split : ", car_number_with_dash.split("-")[0])    # return list of string

first_name = "Aniruddha"
last_name = "Hatgine"
Car_Number = "MH12AB1234"

full_name = " ".join([first_name, last_name,Car_Number])    # return string with space between them 
#print("Full Name : ", full_name)

## Replacing & formatting string


phone_model = "IPhone 12 Pro Max"
#print("Updated Phone Model : ", phone_model.replace("IPhone 12", "iPhone"))    # return string with replaced value

my_name = "Aniruddha"
Car_name = "Honda City"

print(my_name) # simple value print
print("My Name is : ", my_name) # string with variable print

print(f"My name is : { my_name } and my car name is : { Car_name }")                  # string with variable print using format method
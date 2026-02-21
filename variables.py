

# variables
car = "Swift" #string or text , alwasys use "" or '' for string
price = 500000 # integer or numeeric value  
is_new = True  # boolean value (True or False)
mileage = 15.5 # float or decimal value

#print(type(car))

# type() is a built-in function in Python that returns the type of the specified object. 
# It can be used to check the type of a variable or value. 
# In this case, we can use it to check the types of the variables we defined.

# print(type(price))
# print(type(is_new))
# print(type(mileage))

# id() is a built-in function in Python that returns the unique identifier of an object. 
# It can be used to check the memory address of a variable or value.

#print(id(car))
#print(id(price))


a=5
b=a
print(id(a))
print(id(b))
a=7
print(id(a))
print(id(b))




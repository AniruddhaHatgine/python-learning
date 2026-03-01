student_tuple = ("Aniruddha", 20006, 20, "Sangli", "Maharashtra") # used to store multiple values in a single variable

print("Student Tuple : ",type(student_tuple))    # return tuple with all values

#student_tuple[0]="Rahul"

(name, birth_year, age, city, state) = student_tuple  

print("Name : ", name)

color1 = "Red"
color2 = "Green"
print("Color 1 : ", color1)

color1,color2=color2,color1 # swapping of values
print("Color 1 : ", color1)

print("Sangli" in student_tuple)
print(18 in student_tuple)
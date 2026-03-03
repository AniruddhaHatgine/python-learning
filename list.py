Stud_list=["Aniruddha", 20006, 20, "Sangli", "Maharashtra"]
print(type(Stud_list))

#add value
Stud_list.append("India")  # add value at end of list
print(Stud_list)

#pop element

Stud_list.pop()              # remove last element
print(Stud_list)

Stud_list.pop(2)             # remove element by index
print(Stud_list)

Stud_list.remove("Sangli")  # remove element by value
print(Stud_list)

Stud_list.insert(1,"BCA")   #Adding value at specific index
print(Stud_list)

print(Stud_list.reverse())          # reverse the list
print(Stud_list)

print(Stud_list[-1])              # access element by index

num_list=[90,80,40,10,60]
sorted_list= sorted(num_list)            # sort the list in ascending order 
print(sorted_list)

sorted_list= sorted(num_list,reverse=True)            # sort the list in descending order
print(sorted_list)            # sort the list

print(max(num_list))              # return maximum value from list
print(min(num_list))              # return minimum value from list

# sorted()  returns a new sorted list from the items in iterable.
# max() returns the largest item in an iterable or the largest of two or more arguments.
# min() returns the smallest item in an iterable or the smallest of two or more arguments.

color_list=["Red","Green","Blue","Yellow"]
color_list2=["Pink","Purple"]
color_list.extend(color_list2)
print(color_list)

print(color_list+color_list2)

numb_list=[3,5,8,9,3]
numb_list2=[7,4,5,6,9]

print(numb_list+numb_list2)

print(color_list2*3) # print multiple values 

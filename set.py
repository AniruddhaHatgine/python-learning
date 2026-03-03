set_color={"red","green","blue"}

print(type(set_color))

set_color2={"yellow","orange","blue"}


get_all = set_color | set_color2  #union of set1 and set 2


print(get_all)

get_common=set_color & set_color2  # intersection of set1 and set 2
print(get_common)

get_only=set_color - set_color2  # get from set one
print(get_only)


print(set_color.union(set_color2)) 
print(set_color.intersection(set_color2))
print(set_color.difference(set_color2))

print('red' in set_color) #check red color is aval or no

a=frozenset([1,2,3,4])
b=frozenset([3,6,4,9])

sample_set = {a,b}
print(sample_set)
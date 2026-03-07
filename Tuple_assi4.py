ratings=(5,4,3,5,2,5) # tuple is a collection which is ordered and unchangeable. Allows duplicate members.
print("Number of 5-star ratings:",ratings.count(5))

print("First 3-star rating index:",ratings.index(3))

print("Total Ratings:", len(ratings))

print("MAX Rating:", max(ratings))
print("MIN Rating:", min(ratings))

print("Total Score:", sum(ratings))

print("Index num of 2:",ratings.index(2))

print("Count of 4-star rating:",ratings.count(4))

print("Avg Rating:", sum(ratings)/len(ratings))


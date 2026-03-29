revenu = [2500,1200,5000,800,3200,1500]

print ("Total Revenu:" , sum(revenu)) 

print ("Revenu above 2000:" , )

print("revenu abv 2000")

for r in revenu:
    if r >= 2000:
        print(r)
        
count = 0
for r in revenu:
    if r >= 2000:
        count += 1

print("Orders above ₹2000:", count)


print("Max Order:" , max(revenu))


print("Average Revenue:" , sum(revenu)/len(revenu))

for r in revenu:
    if r <= 1000:
        print(r)

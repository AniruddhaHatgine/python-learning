employee={"emp_id":101, "name":"Aniruddha","Department":"IT","salary":50000,"location":"Bangalore"}
print(employee["name"])

employee["salary"]=75000
print(employee)

employee["Gmail"]="rahul@gmail.com"
print(employee)

del employee["location"]
print(employee)

employee["phone"]="4406705805"

employee["Department"]="Software"

print(employee["salary"])

print(len(employee))
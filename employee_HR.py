employee = {
  "emp_id": 101,
  "name": "Ravi Kumar",
  "department": "IT",
  "salary": 55000
}

print(employee["name"])
print(employee.get("department"))

employee["location"] = "Mumbai"

employee.update({"salary":500000})
print(employee)

print(employee.keys())
print(employee.values())
print(employee.items())

print(len(employee))

employee.pop("location")
print(employee)

employee.popitem()

employee_copy=employee.copy()
print(employee)

employee.clear()
print(employee)

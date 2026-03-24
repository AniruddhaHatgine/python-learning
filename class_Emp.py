class employee:
    def dress(self):
        print("Uniform")

    def id(self):
        print("ID")

    def lap(self):
        print("Laptop")

class ITemployee(employee):
    def IT(self):
        print("IT EMP")       

emp=employee()
emp.dress()   
emp.id()        
emp.lap()


#Encapsulation keeps your data locked .Not accesible to outside.

#private variables use '__'before variable.

####################################################

class Car:                                                #class Car → You are creating a blueprint for cars
    def __init__(self,model):                             #__init__ → This runs automatically when you create an object
        self.model = model #public                        #Stores the car model (like "i200")This is public, so you can access it directly
        self.__speed = 0   #private                       #Speed is stored as private__speed means it cannot be accessed directly from outside the class

    def setSpeed(self,speed):                             #This method is used to set/update the speed    /  Since speed is private, you must use this function
        self.__speed=speed
        print("speed:",self.__speed)

    def getSpeed(self):                                   #This method is used to read the speed , Again, because it's private, you can’t access it directly
        return self.__speed
#########################################################

i20 = Car("i200")                                      #You created an object named i20  ,  Model is set to "i200"
i20.setSpeed(20)                                       # set speed to 20

print(i20.model)                                       # print i20
print("Get Speed:",i20.getSpeed())

      
#Create a Class with instance attributes.
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

# Creating an instance of the Person class
person1 = Person(name="ravi", age=25, gender="Male")

# Accessing instance attributes
print(person1.name)  
print(person1.age)   
print(person1.gender) 

#Create a Vehicle class without any variables and methods.
class Vehicle:
    pass
#Creating an instance of the Vehicle class
car = Vehicle()

#Create a child class Bus that will inherit all of the variables and methods of the Vehicle class.
class Vehicle:
    pass
class Bus(Vehicle):
    pass
# Creating an instance of the Bus class
bus = Bus()




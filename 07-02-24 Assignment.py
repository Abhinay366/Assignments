#accessing members of one class inside another class.
#1
class student:
    def __init__(self,stuno,stuname,stumarks):
        self.stuno=stuno
        self.stuname=stuname
        self.stumarks=stumarks
    
    def display(self):
        print("stuno : ",self.stuno)
        print("stuname ",self.stuname)
        print("stumarks : ",self.stumarks)

class Test:
    def modify(stu):
        stu.stuno=stu.stuno+100
        print("printing name inside test class modify method ",stu.stuname)
        stu.display()

a=student(23,"abhi",73)
Test.modify(a)

#2
class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type

class Car:
    def __init__(self, model, engine):
        self.model = model
        self.engine = engine

    def display_info(self):
        print(f"Car Model: {self.model}")
        print(f"Fuel Type: {self.engine.fuel_type}")

my_engine = Engine("Diesel")
my_car = Car("audi", my_engine)

my_car.display_info()

#3
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

my_dog = Dog("tommy")
my_cat = Cat("pilli")

print(f"{my_dog.name} says {my_dog.make_sound()}")
print(f"{my_cat.name} says {my_cat.make_sound()}")

# inner class.
#1
class outer:
    def __init__(self):
        print("outer class object creations")
    
    class Inner:
        def __init__(self):
            print("inner class of creation")
        
        def m1(self):
            print("inner class method")

o=outer()
i=o.Inner()
i.m1()

#2
class OuterClass:
    def __init__(self):
        self.outer_var = "I am an python developer"

    class InnerClass:
        def __init__(self):
            self.inner_var = "I am not an python developer"

o = OuterClass()
i = o.InnerClass()

print(o.outer_var)
print(i.inner_var)

#3
class ShoppingCart:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []

    class Item:
        def __init__(self, product, price):
            self.product = product
            self.price = price

cart = ShoppingCart("Abhi")
item1 = cart.Item("Earphones", 1200)
item2 = cart.Item("mouse", 500)

cart.items.append(item1)
cart.items.append(item2)

for item in cart.items:
    print(f"{item.product}: rs{item.price}")






#using class method 
class MyClass:
    def __init__(self,x,y):
        self.x = x
        self.y= y
        
    @classmethod
    def create_from_str(cls, string):
        x, y = map(int, string.split(","))
        return cls(x, y)
obj = MyClass.create_from_str("3,5")
print(obj.x)  
print(obj.y) 

#2
class Math1:
 def __init__(self,num1,num2):
   self.num1 = num1
   self.num2 = num2
def add(self):
    return self.num1 + self.num2
obj1 = Math1(10,20)
sum1= obj1.add()
print('Suml =',sum1)
obj2 = Math1(40,60)
sum2 = obj2.add()
print('Sum2=',sum2)

#without using 
class MyClass:
    def __init__(self, abc):
        x, y = map(int, abc.split(","))
        self.x = x
        self.y = y
    
    def display(self):
        print(self.x)
        print(self.y)
obj = MyClass("4,5")
obj.display()

#2
class fed:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self, num):
        return fed(num, num)    
obj1 = fed.display(6,8)
print(obj1.x)  
print(obj1.y)



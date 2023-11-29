#write down 6 differences between pop(),remove(),discard().
#Pop()                                        Remove()                                                      Discard()
#1.The pop() function                1.remove() function removes the first             1.It is a set method used to remove a specified 
#removes the last                    occurrence of the specified element.             element  from a set if the element is present
#removes the last                                                                      If the element is not present, it doesn't 
#element or the element based                                                           raise an error and simply does nothing.
#on the index given.

#2.It does not require a             2.It requires a parameter. The value              2.discard() does not raise a KeyError if the element is not found in the set. 
#parameter; it is optional.          of the element is passed as the parameter.          element is not found in the set.

#3.It returns the value              3.It does not return any value.                   3.Itdoesn't return any value. It directly modifies 
#of the deleted element.                                                                the set it is called on by removing the specified element, if present.

#4.It gives IndexError if the        4.It gives ValueError if the specified            4.discard() is commonly used with mutable sets.
#specified index is not found.       value is not found.

#5.It gives no error if the          5.It throws TypeError if                          5.While discard() and remove() both remove elements from sets, 
#parameter is not passed.            the parameter is not passed.                       the key difference lies in the behavior when the element is not present. 
#                                                                                       remove() raises an error, while discard() does not.

#6.Time complexity is O(1) when      6.Time complexity is O(n)                         6.This method is efficient for scenarios where you want to remove 
#the last element is to be removed.                                                     an element if it exists in a set without having to check for 
#Otherwise, it is O(n) for extracting                                                    its existence separately, thus streamlining the code.
#an element at the specified index.

#write a pro to take tuple of numbers from keyboard and print Sum,avg.
tuple=(10,20,30,40,50,60,70,80,90)
print(len(tuple))
avg=len(tuple)
sum=0
for i in tuple:
    sum=sum+i
print(sum/avg)

t=(10,20,30,40,50,60,70,80,90,100,101)
sum=0
for i in t:
    sum=sum+i
print(sum)

#All methods examples.
#Using upper()function.
Message="Abhi is a python developer"
print(Message.upper())

#Using lower()function.
Message="Abhi is a python developer"
print(Message.lower())

#Using swapcase()function.
Message="Abhi is a python developer"
print(Message.swapcase())

#Using title()function.
Message="Abhi is a python developer"
print(Message.title())

#Using capitalize()function.
Message="Abhi is a python developer"
print(Message.capitalize())

#Using insert() Function.
l = ['carrot', 'brinjal', 'tomato'] 
l.insert(-2, 'potato') 
print(l)  

l = ['carrot', 'brinjal', 'tomato'] 
l.insert(3, 'potato') 
print(l)  

l = [0,1,2] 
s= {3,4,5} 
l.insert(3,s) 
print(l) 

l = [ 1, 2, 3, 4, 5, 6, 7 ]  
l.insert(4, 10)  
print(l)  

s = ['Sun', 'looks', 'like', 'an', 'cirlcle'] 
s.insert(0, "The") 
print(s)

#Using append() Function.
a = ['cat', 'dog', 'rabbit']
w = ['tiger', 'fox']
a.append(w)
print('Updated animals list: ', a)

m = ['boy', 'for', 6, 0, 4, 1]
m.extend('abhi')
print(m)

l = [ 1, 2, 3, 4, 5, 6, 7 ]  
l.append(40)  
print(l)  

s = ['Abhi', 'is', 'a', 'python'] 
s.append("developer") 
print(s)

l = ['carrot', 'brinjal', 'tomato'] 
l.append('potato') 
print(l)  

#Using count() function.
p = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = p.count(9)
print(x)

txt="Abhi is a python Developer"
x=txt.count('python')
print(x)

l= ['a', 'a', 'a', 'b', 'b', 'a', 'c', 'b'] 
print(l.count('b'))

l = [ ('Cat', 'Bat'), ('Sat', 'Cat'), ('Cat', 'Bat'),
          ('Cat', 'Bat', 'Sat')]
print(l.count(('Cat', 'Bat')))

s=['Abhi','boy',123,123]
x=s.count(123)
print(x)

#Using index() Function.
l = [6, 8, 5, 6, 1, 2] 
print(l.index(6, 1)) 

l = ['cat', 'bat', 'mat', 'cat', 'pet'] 
print(l.index('bat')) 

l=[10,20,30,40,90]
print(l.index(90))

s=['Abhi','boy',123,123]
x=s.index(123)
print(x)

s=['Abhi','phani','Rahul','ravi']
print(s.index('ravi'))

#Using Lstrip function.
txt = "     banana     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")

my_string = "   Hello, world!   "
stripped_string = my_string.lstrip() 
print(stripped_string)

message = '     Learn Python  '
print('Message:', message.lstrip())

str = "xxXXX this is string example XXXXXxxxxx";
print(str.lstrip('x'))

string = "++++x...y!!z* my name is abhi"
print(string.lstrip("+.!*xyz"))

#Using Rstrip function.
txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")

my_string = "   Hello, world!   "
stripped_string = my_string.rstrip() 
print(stripped_string)

message = '     Learn Python  '
print('Message:', message.rstrip())

str = "xxXXX this is string example XXXXXxxxxx";
print(str.rstrip('x'))

string = " my name is abhi ++++x...y!!z*"
print(string.rstrip("+.!*xyz"))

#Usinf find function.
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)

txt = "Hello, welcome to my world."
x = txt.find("e")
print(x)

message = 'Python is a fun programming language'
print(message.find('fun'))

word = 'Bugs for Bugs'
print(word.find('Bu', 2))

word='Hello World'
print(word.find('h'))  

#Using Rfind function.
txt = "Hello, welcome to my world."
x = txt.rfind("welcome")
print(x)

txt = "Hello, welcome to my world."
x = txt.rfind("e")
print(x)

message = 'Python is a fun programming language'
print(message.rfind('fun'))

word = 'Bugs for Bugs'
print(word.rfind('Bu', 2))

word='Hello World'
print(word.rfind('h'))  


# Using pop() function
my_list = [1, 2, 3, 4, 5]
removed_element = my_list.pop(2)
print("Removed element:", removed_element)
print("Updated list:", my_list)

my_list = [10, 20, 30, 40, 50]
last_element = my_list.pop()  
print("Removed element:", last_element)
print("Updated list:", my_list)

my_list = ['a', 'b', 'c', 'd', 'e']
while my_list:
    removed = my_list.pop() 
    print("Removed:", removed)
    print("Updated list:", my_list)

empty_list = []
try:
    element = empty_list.pop(2)  
    print("Element removed:", element)
except IndexError as e:
    print("IndexError occurred:", e)

numbers = [11, 22, 33, 44, 55, 66, 77, 88]
index = 0
while index < len(numbers):
    if numbers[index] > 50:
        removed = numbers.pop(index)  
        print(f"Removed {removed} at index {index}")
    else:
        index += 1
print("Updated list:", numbers)

#Using remove() function.
l = ['Alice', 'Bob', 'Charlie', 'Bob', 'Dave']
l.remove('Alice')
print(l)

l = ['Alice', 'Bob', 'Charlie', 'Bob', 'Dave']
l.remove('Bob')
print(l)

#Using delete() Function.
l = [0, 10, 20, 30, 40, 50]
del l[0]
print(l)

l = [0, 10, 20, 30, 40, 50]
del l[-1]
print(l)

l = [0, 10, 20, 30, 40, 50]
del l[2:5]
print(l)

l = [0, 10, 20, 30, 40, 50]
del l[:3]
print(l)

l = [0, 10, 20, 30, 40, 50]
del l[:]
print(l)

#Using discard() function.
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)

numbers = {2, 3, 4, 5}
numbers.discard(3) 
print(numbers)

numbers = {2, 3, 4, 5}
numbers.discard(3)
print('Set after discard:', numbers)

numbers = {2, 3, 5, 4}
print('Set before discard:', numbers)
numbers.discard(10)
print('Set after discard:', numbers)

numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(numbers)
numbers.discard(5)
print(numbers)

#Using update() function.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y)
print(x)

marks = {'Physics':67, 'Maths':87}
internal_marks = {'Practical':48}
marks.update(internal_marks)
print(marks)

d = {1: "one", 2: "three"}
d1 = {2: "two"}
d.update(d1)
print(d)
d1 = {3: "three"}
d.update(d1)
print(d)

dictionary = {'x': 2}
dictionary.update([('y', 3), ('z', 0)])
print(dictionary)

dictionary = {1: 'Student',
'Name': 'Abhinay',
'Subjects': 'Computers'}
dictionary.update({'University':'KL'})
print(dictionary)



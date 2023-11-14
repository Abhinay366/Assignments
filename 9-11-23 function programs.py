#strip function.
txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")

my_string = "   Hello, world!   "
stripped_string = my_string.strip() 
print(stripped_string)

message = '     Learn Python  '
print('Message:', message.strip())

str = "xxXXX this is string example XXXXXxxxxx";
print(str.strip('x'))

string = "++++x...y!!z* my name is abhi"
print(string.strip("+.!*xyz"))

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

#Using index function
fruits = ['apple', 'banana', 'orange']
x = fruits.index("orange")

fruits = [4, 55, 64, 32, 16, 32]
x = fruits.index(32)

txt = "Hello, welcome to my world."
print(txt.index("w"))

txt = "Hello, welcome to my world."
x = txt.index("e")
print(x)

text = 'Python is fun'
result = text.index('is')
print(result)

#Using slice operator.
a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(2)
print(a[x])

a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(3, 5)
print(a[x])

l = ['a', 'b', 'c', 'd', 'e', 'f']
s = slice(-2, -6, -1)
print("list slicing:", l[s])

String = 'Hello World'
x = slice(5,11)
print(String[x])

s = "Abhinay"
b = slice(-1)
print("string slicing:", s[b])

slice_numbers = [1, 2, 3, 4, 5]
print("slice_number before slicing and modfication : ",end=' ')
print(slice_numbers) 
slice_numbers[1:4] = [10, 20, 30]
print("slice_number after slicing and modfication : ",end=' ')
print(slice_numbers) 

py_string = 'Python'
print(py_string[0:3])
print(py_string[1:5:2])

myStr = 'Hello! How are you?'
print("String = ",myStr)
print("String after slicing = ",myStr[8:15:2])













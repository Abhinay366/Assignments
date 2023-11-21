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

#Accessing list of elements using for loop.
l = [1, 3, 5, 7, 9]
for i in l:
    print(i)

l= [1, 3, 5, 7, 9]
s = len(l)
for i in range(s):
    print(l[i])

l= [10, 21, 4, 45, 66, 93]
for num in l:
    if num % 2 == 0:
        print(num, end=" ")

#Accessing list of elements using while loop.
l = [1, 3, 5, 7, 9]
i = 0
while i < len(l):
    print(l[i])
    i += 1

l = [4, 52, 6, 9, 21]
i = 0
while i < len(l) :
    print(l[i])
    i+= 1

l = [4, 52, 6, 9, 21]
i = len(l) - 1
while i >= 0 :
    print(l[i])
    i-= 1

l=['a','b','c','d','e']
a=len(l)
for i in range(a):
    print(l[i]," is available at +ve index is ",i, " and at -ve index is ",i-a)












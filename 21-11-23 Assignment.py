#Difference between remove() and pop().
    #Remove()                                        Pop()
#1.It is a method.                             1.pop() is a method.

#2.To delete value this method                 2.This method also uses the index as a parameter to delete.
#uses the value as a parameter.

#3.The remove() method doesn’t return any      3.pop() returns deleted value.
#value.

#4.At a time it deletes only one value from    4.At a time it deletes only one value from the list.
#the list.

#5.It throws value error in case of value      5.It throws index error in case of an index doesn’t exist in the list.
#doesn’t exist in the list.

#Using extend() Function.
Name = ['Abhi', 'Phani', 'Ravi']
c = ['Ford', 'BMW', 'Volvo']
Name.extend(c)
print(Name)

a1 = [1, 2]
a2 = [1, 2]
b = (3, 4)
a1.extend(b) 
print(a1)
a2.append(b)
print(a2)

l = [1, 2, 3] 
l.extend([4, 5, 6]) 
print(l)

l = ['abhi', 'is', 6, 0, 4, 1] 
l.extend('abhi') 
print(l)

l=['Abhi','is','a','developer']
n=[-1,7,-9]
l.extend(n)
print(l)

#Using remove() Function.
prime_numbers = [2, 3, 5, 7, 9, 11]
prime_numbers.remove(9)
print(prime_numbers)

animals = ['cat', 'dog', 'rabbit', 'guinea pig']
animals.remove('rabbit')
print(animals)

l = ['a', 'b', 'c'] 
l.remove("b") 
print(l)

l1 = [ 1, 2, 1, 1, 4, 5 ]  
l1.remove(1)  
print(l1)   
l2 = [ 'a', 'b', 'c', 'd' ]  
l2.remove('a')  
print(l2)

l = [ 'a', 'b', 'c', 'd', 'd', 'e', 'd' ] 
l.remove('d') 
print(l)

#Using pop() Function.
l = [1, 2, 3, 4, 5, 6] 
print(l.pop(3), l)

l= [1, 2, 3, 4, 5, 6] 
print(l.pop(-2))

languages = ['Python', 'Java', 'C++', 'French', 'C']
print(languages.pop(3))

l = [ 'a', 'b', 'c', 'd', 'd', 'e', 'd' ] 
l.pop(5) 
print(l)

l1 = [ 1, 2, 1, 1, 4, 5 ]  
l1.pop(1)  
print(l1)   
l2 = [ '-1', '-2', '-3', '-4' ]  
l2.pop(2)  
print(l2)






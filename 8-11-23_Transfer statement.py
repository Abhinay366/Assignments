#Using break statement
for i in range(10): 
    print(i) 
    if i == 7: 
        break

market = ["Apple", "Orange", "Grapes"]
for x in market:
  print(x)
  if x == "Orange":
    break
  
  i = 1
while i <= 10:
    print('6 * ',(i), '=',6 * i)
    if i >= 5:
        break
    i = i + 1

s = 'Hello, World!'
for char in s:
    print(char)
    if char == ',':
        break

num = 0
for number in range(10):
    if number == 5:
        break 
    print('Number is ' + str(number))
print('Out of loop')

#Using continue statement
i = 0
while i < 10:
    if i == 5:
        i += 1
        continue
    print(i)
    i += 1

for i in range(1, 11):
    if i == 6:
        continue
    else:
         print(i, end=" ")

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in nested_list:
    for j in i:
        if j == 3:
            continue
        print(j)

num = (1,2,3,4,5,6,7,8)
count = 8
while (count>0):
  count = count-1
  if count == 4:
     continue
  print (num[count])
print ('End of program')

for letter in 'YOLO':
  if letter == 'L':
    continue
  print (letter)

#Using pass statement
n = 10
if n > 10:
    pass
print('abhi')

list =['a', 'b', 'c', 'd']
for i in list:
    if(i =='a'):
        pass
    else:
        print(i)

a = 10
b = 20
if(a<b):
  pass
else:
  print("b<a")

for letter in 'Python':
   if letter == 'h':
      pass
      print ('This is pass block')
   print ('Current Letter :', letter)
print ("Good bye!")
for i in range(100):
  if i%20==0:
      print(i)
  else:
      pass
print("abhi")

l1=["A","B","c"]
l2=["A","B","c"]
print(l1==l2)

s="this is gopi and my name is gopi"
print(s.find('gopi',14,20))

  

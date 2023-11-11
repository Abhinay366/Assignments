#1.program to display numbers from 1 to 5.
i = 1
n = 5
while i <= n:
    print(i)
    i = i + 1

#2.program to calculate the sum of numbers until the user enters zero.
total = 0
number = int(input('Enter a number: '))
while number != 0:
    total += number   
    number = int(input('Enter a number: '))
    print('total =', total)

#3.program using infinite while loop.
age = 17
while age > 18:
    print('You can vote')

#4.program using while loop with else.
counter = 0

while counter < 3:
    print('Inside else')
    counter = counter + 1
else:
    print('Outside else')

#5.program using while loop with break statement.
counter = 0
while counter < 3:
    if counter == 1:
        break
    print('Abhi')
    counter = counter + 1
else:
    print('Nothing')

#6.program while loop on boolean values.
count = 0
while True:
    count += 1
    print(f"Count is {count}")
    if count == 10:
        break
print("The loop has ended.")

#7.program  while loop with a pass statement.
a = 'acknowledge'
i = 0
while i < len(a):
    i += 1
    pass
print('Value of i :', i)

#8.program to display numbers less than 5.
i = 1
while i < 5:
  print(i)
  i += 1

#9.progarm on while loop.
count = 0
while (count < 3):
    count = count + 1
    print("Hello abhi")

#10.Python while loop with continue statement.
i = 0
a = 'boomboomboomer'
while i < len(a):
    if a[i] == 'o' or a[i] == 'm':
        i += 1
        continue
    print('Current Letter :', a[i])
    i += 1

#11.Popping out elements from a list using while loop
fruitsList = ["Mango","Apple","Orange","Guava"]
while fruitsList:
    print(fruitsList.pop())
print(fruitsList)

#12.Finding the average of 5 numbers using while loop.
p = 5
sum = 0
count = 0
while p > 0:
    count += 1
    f = int(input("Enter the number "))
    sum += f
    p -= 1
average = sum/count
print("Average of given Numbers:",average)
         
#13.Python while loop to print a number series.
n = 10
while n <= 100:
    print(n ,end = ",")
    n = n+10

#14.Adding elements to a list using while loop.
myList = []
i = 0
while len(myList) < 4 :
    myList.append(i)
    i += 1
print(myList)

#15.Printing the items in a tuple using while loop.
myTuple = (10,20,30,40,50,60)
i = 0
while i < len(myTuple):
    print(myTuple[i])
    i += 1

#16.Finding the sum of numbers in a list using while loop.
myList = [23,45,12,10,25]
i = 0 
sum = 0
while i < len(myList):
    sum += myList[i]
    i += 1
print(sum)

#17.Printing the square of numbers using while loop.
n = 1
while n <= 5:
    squareNum = n**2
    print(n,squareNum)
    n += 1

#18.Finding the multiples of a number using while loop.
n = int(input("Enter an integer: "))
i = 1
while i <= 10:
    mul = i*n
    i += 1
    print(mul)

#19.Finding the sum of even numbers using while loop.
i = 0
sum = 0
n = int(input("Enter the number n: "))
while  i <= n:
    if i % 2 == 0:
        sum += i
    i += 1
    print("Sum of even numbers till n:",sum)

#20.Converting numbers from decimal to binary using while loop.
num = int(input("Enter a number: "))
b = 0
p = 1
n = num
while n>0:
    rem = n%2
    b += rem * p
    p = p*10
    n = n//2
print("Binary value: ",b)




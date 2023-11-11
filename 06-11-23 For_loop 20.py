#1.Print the first 10 natural numbers using for loop.
n=10
for i in range(1,n):
        print(i)

#2.Python program to print all the even numbers within the given range.
given_range = 10
for i in range(given_range):
     if i%2==0:
          print(i)

#3.Python program to calculate the sum of all numbers from 1 to a given number.
given_number = 10
sum = 0
for i in range(1,given_number+1):
        sum+=i
print(sum) 

#4.Python program to calculate the sum of all the odd numbers within the given range.
given_range = 10
sum = 0
for i in range(given_range):
        if i%2!=0:
                sum+=i
print(sum)

#5.Python program to print a multiplication table of a given number.
given_number = 6
for i in range(11):
        print (given_number," x",i," =",5*i)

#6.Python program to display numbers from a list using a for loop.
list = [1,2,4,6,88,125]
for i in list:
    print(i)

#7.Python program to count the total number of digits in a number.
given_number = 129475
given_number = str(given_number)
count=0
for i in given_number:
        count += 1
        print(count)

#8.You are given a list of integer elements. Make a new list that will store squares of elements from the previous list.
numbers=[1,2,4,6,7,8]
b=[]
for i in numbers:
      b.append(i**2)
      print(b)

#9.Print individual letters of a string using the for loop.
word="anaconda"
for letter in word:
	print (letter)
      
#10.Using the for loop to iterate over a Python list or tuple.
words= ["Apple", "Banana", "Car", "Dolphin" ]
for word in words:
	print (word)

#11.we have a list of numbers and we want to print the sum of positive numbers.
nums = [1, 2, -3, 4, -5, 6]
sum_positives = 0
for num in nums:
    if num < 0:
        continue
    sum_positives += num
print(f'Sum of Positive Numbers: {sum_positives}')

#12.we have a function to print the sum of numbers if and only if all the numbers are even.
def print_sum_even_nums(even_nums):
    total = 0
for x in numbers:
        if x % 2 != 0:
            break
        total += x
else:
        print("For loop executed normally")
        print(f'Sum of numbers {total}')

#13.Write a program select even and odd numbers in a given list and we will put them in different lists.
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even = []
odd = []
for x in numbers:
  if (x % 2 == 0):
               even.append(x)
  else:
               odd.append(x)
print("Even numbers:", even)
print("Odd numbers:", odd)

#14.Write a program to see a number whose square is higher than 40, the code will end the loop. Until the end, the code will print the square of the numbers.
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
for x in numbers:
  if (x*x > 40):
    break
  print(x*x)

#15.Write a program to  control that if lour item is equal to 5 or 7. If it is equal one of them, then we will not print the square of it.
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
for x in numbers:
  if (x == 5):
    continue
  if (x == 7):
    continue
  print(x*x)

#16.Write a program if it is even and then we will print the square of these even numbers.
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
for x in numbers:
  if (x % 2 == 0):
   print(x*x)

#17.Write a program for loop in Python is used to iterate over a sequence, which could be a list.
colours=["red","Green","Blue","yellow"]
for x in colours:
      print(x)
s="red"
for x in s:
      print(x)
 
 #18.Write a program in the given list the number is less than zero to pass the statement.
nums = [1, 3, 5, 16, -7, 9, 7]
for num in nums:
 if num < 0:
   print("I found a pass statement!")
pass
print(num)

#19.Write a program in the given list the numbers should be reverse.
nums = [1, 3, 5, 16, -7, 9, 7]
for num in reversed(nums):
  print(num)

#20.Write a program to find the range in the given list.
numbers = [1, 9, 5]
for i in range(len(numbers)):
  print(i)
 



 





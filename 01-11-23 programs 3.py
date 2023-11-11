#1.Write a program to find the biggest of given 2 numbers from the keyboard.
num1,num2=35,90
print((num1 if num1>num2 else num2))

#2.Write a program to check whether the given number is in between 1 to 100.
x= int(input("Enter a number:"))
if x>=1 and x<=100:
     print('Entered number',x,"is lies between 1 and 100.")
else:
     print('Entered number',x,"is does not lies between 1 and 100.")

#3.Write a program some digit entered by user and it should be in words.
def printWord(N): 
    digits={'1':'One','2':'Two','3':'Three','4':'Four','5':'Five','6':'Six','7':'Seven','8':'Eight','9':'Nine','0':'Zer0'}
    for number in N:
         print(digits[number], end =' ')
N="123479"
printWord(N)

num1,num2=35,40















#1.Half pyramid pattern using stars.
n = 5
for i in range(5):
    for j in range(1, i+1):
        print("*", end="  ")
    print()

#2.Full Triangle pyramid using stars.
rows = 5
n = (2 * rows) - 2
for i in range(0, rows):
    for j in range(0, n):
        print(end=" ")
    
    n = n - 1
    for j in range(0, i + 1):
        print("* ", end=' ')
    print(" ")

#3.Half inverted pyramid using stars.
n=5
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print("*",end="  ")
    print()

#4.Right Half diamond shape using stars.
n = 5
for i in range(5):
    for j in range(1, i+1):
        print("*", end="  ")
    print()

n=5
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print("*",end="  ")
    print()

#5.Left half diamond shape using stars.
rows = 5
i = 1
while i <= rows:
    j = i
    while j < rows:
        print(' ', end=' ')
        j += 1
    k = 1
    while k <= i:
        print('*', end=' ')
        k += 1
    print()
    i += 1

i = rows
while i >= 1:
    j = i
    while j <= rows:
        print(' ', end=' ')
        j += 1
    k = 1
    while k < i:
        print('*', end=' ')
        k += 1
    print('')
    i -= 1

#6.Right down mirror star pattern.
rows = 5
i = rows
while i >= 1:
    j = rows
    while j > i:
        print(' ', end=' ')
        j -= 1
    k = 1
    while k <= i:
        print('*', end=' ')
        k += 1
    print()
    i -= 1

#7.diamond shape pattern using stars.
rows = 5
k = 2 * rows - 2
for i in range(0, rows):
    for j in range(0, k):
        print(end=" ")
    k = k - 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")
    
k = rows - 2
for i in range(rows, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")

#8.Sandglass pattern of star.
row=5
for i in range(row, 0, -1):
    for j in range(row-i):
        print(" ", end="")
    for j in range(1, 2*i):
        print("*", end="")
    print()
for i in range(2, row+1):
    for j in range(row-i):
        print(" ", end="")
    for j in range(1, 2*i):
        print("*", end="")
    print()

#9.Pant style pattern of stars.
rows = 10
print("*" * rows, end="\n")
i = (rows // 2) - 1
j = 2
while i != 0:
    while j <= (rows - 2):
        print("*" * i, end="")
        print("_" * j, end="")
        print("*" * i, end="\n")
        i = i - 1
        j = j + 2

#10.Square pattern using stars.
rows = 5
for i in range(1,rows+1):
    for j in range(1,rows+1):
        print("*", end=" ")
    print()

#11.Rectangle pattern using stars.
row=5
col=10
for i in range(1,row+1):
    for j in range(1,col+1):
        print("*", end="")
    print()

#12.Hallow diamond pattern using stars.
row=5
for i in range(1, row+1):
    for j in range(1,row-i+1):
        print(" ", end="")
    for j in range(1, 2*i):
        if j==1 or j==2*i-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
for i in range(row-1,0, -1):
    for j in range(1,row-i+1):
        print(" ", end="")
    for j in range(1, 2*i):
        if j==1 or j==2*i-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

#13.Butter fly pattern using stars.
row = int(input("Enter number of rows (even): "))
n = row//2
print("Generated butterfly pattern is:\n")
for i in range(1,n+1):
    for j in range(1, 2*n+1):
        if j>i and j< 2*n+1-i:
            print("  ", end="")
        else:
            print("* ", end="")
    print()

for i in range(n,0,-1):
    for j in range(2*n,0,-1):
        if j>i and j< 2*n+1-i:
            print("  ", end="")
        else:
            print("* ", end="")
    print()   

#14.Hollow Pyramid Pattern using stars.
row=6
for i in range(row,0,-1):
    for j in range(row-i):
        print(' ', end='') 
    
    for j in range(2*i-1):
        if i==0 or i==row or j==2*i-2 or j==0:
            print('*',end='') 
        else:
            print(' ', end='') 
    print() 

#15.Hollow Hour-glass Pattern using stars.
row=7
for i in range(row, 0, -1):
    for j in range(row-i):
        print(" ", end="")
    for j in range(1, 2*i):
        if i==1 or i==row or j==1 or j==2*i-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

for i in range(2, row+1):
    for j in range(row-i):
        print(" ", end="")
    for j in range(1, 2*i):
        if i==1 or i==row or j==1 or j==2*i-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

#16.Cross pattern using stars.
n=7
for i in range(1,2*n):
    for j in range(1,2*n):
        if i==j or i+j==2*n:
            print('*', end='')
        else:
            print(' ', end='')
    print()

#17.Asterisk Pattern using stars.
n=6
for i in range(1,2*n):
    for j in range(1,2*n):
        if j==n or i==j or i+j==2*n:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

#18.Hollow Right Angle Triangle Pattern Using Stars.
row=5
for i in range(row):
    for j in range(i+1):
        if j==0 or j==i or i==row-1:
            print('*',end=" ")
        else:
            print(" ", end=" ")
    print()

#19.Plus Pattern using stars.
n=6
for i in range(1,2*n):
    for j in range(1,2*n):
        if i==n or j==n:
            print('*', end='')
        else:
            print(' ', end='')
    print()

#20.Hallow pyramid using stars.
row=6
for i in range(row):
    for j in range(row-i):
        print(' ', end='') 
    
    for j in range(2*i+1):
        if j==0 or j==2*i or i==row-1:
            print('*',end='')
        else:
            print(' ', end='')
    print() 

#21.Print two pyramids of stars.
rows = 6
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print(" ")
print(" ")

for i in range(rows + 1, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")

#22.right-angled pattern with characters.
ascii_number = 65
rows = 7
for i in range(0, rows):
    for j in range(0, i + 1):
        character = chr(ascii_number)
        print(character, end=' ')
        ascii_number += 1
    print(" ")

#23.Pattern to display letter of the word.
word = "Abhinay"
x = ""
for i in word:
    x += i
    print(x)

#24.Pyramid of horizontal number tables.
rows = 7
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(i * j, end=' ')
    print()

#25.Double the number pattern.
rows = 9
for i in range(1, rows):
    for j in range(-1 + i, -1, -1):
        print(format(2 ** j, "4d"), end=' ')
    print("")

#26.Random number pattern.
rows = 9
for i in range(1, rows):
    for i in range(0, i, 1):
        print(format(2 ** i, "4d"), end=' ')
    for i in range(-1 + i, -1, -1):
        print(format(2 ** i, "4d"), end=' ')
    print("")

#27.Pyramid of numbers less than 20.
current_num = 1
stop = 2
rows = 4

for i in range(rows):
    for column in range(1, stop):
        print(current_num, end=' ')
        current_num += 1
    print("")
    stop += 2

#28.Pattern double number on each column.
rows = 7
for i in range(0, rows):
    for j in range(0, i + 1):
        print(i * j, end='  ')
    print()

#29.Number reduction pattern.
rows = 5
for i in range(0, rows + 1, 1):
    for j in range(i + 1, rows + 1, 1):
        print(j, end=' ')
    print()

#30.Pattern with a combination of numbers and stars.
row = 4
for i in range(0, row):
    c = 1
    print(c, end=' ')
    for j in range(row - i - 1, 0, -1):
        print('*', end=' ')
        c = c + 1
        print(c, end=' ')
    print('\n')

#31.Unique pyramid pattern of digits.
rows = 6
for i in range(1, rows + 1):
    for j in range(1, i - 1):
        print(j, end=" ")
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()

#32.Even number pattern.
rows = 5
last_num = 2 * rows
even_num = last_num
for i in range(1, rows + 1):
    even_num = last_num
    for j in range(i):
        print(even_num, end=' ')
        even_num -= 2
    print("\r")

#33.Repeated number pattern.
num = 4
counter = 0
for x in range(0, num):
    for y in range(0, x + 1):
        print(counter, end=" ")
        counter = 2 ** (x + 1)
    print()

#34.Pattern of same character.
character = 'V'
char_ascii_no = ord(character)
for i in range(0, 5):
    for j in range(0, i + 1):
        user_char = chr(char_ascii_no)
        print(user_char, end=' ')
    print()

#35.Pyramid pattern of numbers.
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print('')

#36.Inverted pyramid pattern of numbers.
rows = 5
b = 0
# reverse for loop from 5 to 0
for i in range(rows, 0, -1):
    b += 1
    for j in range(1, i + 1):
        print(b, end=' ')
    print('\r')

#37.Inverted Pyramid pattern with the same digit.
rows = 5
num = rows
# reverse for loop
for i in range(rows, 0, -1):
    for j in range(0, i):
        print(num, end=' ')
    print("\r")

#38.Another inverted half-pyramid pattern with a number.
rows = 5
for i in range(rows, 0, -1):
    for j in range(0, i + 1):
        print(j, end=' ')
    print("\r")

#39.Alternate numbers pattern using a while loop.
rows = 5
i = 1
while i <= rows:
    j = 1
    while j <= i:
        print((i * 2 - 1), end=" ")
        j = j + 1
    i = i + 1
    print('')

#40.Reverse number pattern1.
rows = 5
for i in range(rows, 0, -1):
    num = i
    for j in range(0, i):
        print(num, end=' ')
    print("\r")

#41.Reverse Pyramid of Numbers.
rows = 6
for i in range(1, rows):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print("")

#42.Another reverse number pattern.
rows = 5
for i in range(0, rows + 1):
    for j in range(rows - i, 0, -1):
        print(j, end=' ')
    print()

#43.Number triangle pattern.
rows = 6
for i in range(1, rows):
    num = 1
    for j in range(rows, 0, -1):
        if j > i:
            print(" ", end=' ')
        else:
            print(num, end=' ')
            num += 1
    print("")

#44.Square pattern with numbers.
rows = 5
for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        if j <= i:
            print(i, end=' ')
        else:
            print(j, end=' ')
    print()

#45.Multiplication table pattern.
rows = 8
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        square = i * j
        print(i * j, end='  ')
    print()

#46.Simple Number Triangle Pattern.
rows = 6
for num in range(rows):
    for i in range(num):
        print(num, end=" ") 
    print(" ")

#47. Inverted Pyramid of Numbers.
rows = 5
b = 0
for i in range(rows, 0, -1):
    b += 1
    for j in range(1, i + 1):
        print(b, end=' ')
    print('\r')

#48.Inverted Pyramid of Descending Numbers.
rows = 5
for i in range(rows, 0, -1):
    num = i
    for j in range(0, i):
        print(num, end=' ')
    print("\r")

#49.Inverted Pyramid of the Same Digit.
rows = 5
num = rows
for i in range(rows, 0, -1):
    for j in range(0, i):
        print(num, end=' ')
    print("\r")

#50. Pyramid Pattern of Alternate Numbers.
rows = 5
i = 1
while i <= rows:
    j = 1
    while j <= i:
        print((i * 2 - 1), end=" ")
        j = j + 1
    i = i + 1
    print()




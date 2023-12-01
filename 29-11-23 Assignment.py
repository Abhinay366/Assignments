#Write a program to print different vowels present in the given word and count of vowels.
a=input("Enter string: ")
count=0
vowels=set("aeiou")
for letter in a:
    if letter in vowels:
        count+=1
print("count of the vowels is: ",count)

#Write a program to enter the name and % of marks in a dict and display info on the screen. 
stu_info={}
n = int(input("Enter number of students: "))
for i in range(n):
  name = input(f"Enter student {i+1} name: ")
  marks = float(input(f"Enter {name}'s percentage of marks: "))
  stu_info[name] = marks
#To Display student information. 
  print("\nStudent Information:")
  print("Name\t\tPercentage")
  for name, marks in stu_info.items():
     print(f"{name}\t\t{marks}")







str1=input("enter the sentence:")
words=str1.split()
rev_words=words[::-1]
sen=" ".join(rev_words)
print(sen)

def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str
s = "Rangerover is a beast"
print("The original string is : ", end=" ")
print(s.split())
print("The reversed string(using loops) is : ", end=" ")
print(reverse(s))

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

s=input("enter the string : ")
subs=input("enter the sub string :")
flag=False
position=-1
n=len(s)
while True:
    position=s.find(subs,position+1,n)
    if position==-1: 
        break
    print("found at index :",position)
    flag=True
if flag==False:
    print("NOT found")







#write a program to display unique vowels present in the given words.
text="python is not easy untill we will practice"
l=[char for char in text if char in "aeiou"]
print(len(l))
print(l)
print()

text="abhi is a python developer"
for char in text:
    if char.lower() in 'aeiou':
        print(char)

#Take two list compreshisve l1 and l2 in the l1 do some action and use that l1 in l2.
l1=[x*x for x in range(1,11)]
print(l1)
l2=[i for i in l1 if i%2==0]
print(l2)

#square root of range from 1 to 20.
l=[x*x for x in range(1,21)]
print(l)












#import zip file.
a=open("fruits.txt","w")
b=open("flowers.txt","w")
c=open("names.txt","w")

from zipfile import *
f=ZipFile("abhinay.zip","w")
f.write("list.txt")
f.write("ravi.txt")
f.write("names.txt")
f.write("student.csv")
f.close()
print("zip file is created")



from zipfile import *
f=ZipFile("abhinay.zip","r")
names=f.namelist()
for i in names:
    print("filename is ", i)
    f1=open(i,"r")
    print(f1.read())
    print()
f=ZipFile("abhinay.zip","w")
f.write("list.txt")
f.write("ravi.txt")
f.write("names.txt")
f.write("student.csv")
f.close()
print("zip file is created")




import os
cwd=os.mkdir("abhinay/file")


import os
cwd=os.makedirs("abhinay/file/file1/file2/file3")


import os
os.mkdir("abhinay/file1")
os.mkdir("abhinay/file2")
os.mkdir("abhinay/file3")
os.mkdir("abhinay/file4")


import os
os.rmdir("abhinay/file1")


import os
print(os.listdir("abhinay"))

#File Handling
#r: open an existing file for a read operation.
#w: open an existing file for a write operation. If the file already contains some data, then it will be overridden but if the file is not present then it creates the file as well.
#a: open an existing file for append operation. It won’t override existing data.
#r+:To read and write data into the file. The previous data in the file will be overridden.
#w+:To write and read data. It will override existing data.
#a+:To append and read data from the file. It won’t override existing data.
#x: Creates the specified file, returns an error if the file exists.
    
file = open('abhi.txt', 'r')
 # This will print every line one by one in the file
for each in file: 
    print (each)

with open("file.txt", "w") as f: 
    f.write("Hello World!!!")

file = open("file.txt", "r") 
print (file.read())

f = open("file2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("file2.txt", "r")
print(f.read())



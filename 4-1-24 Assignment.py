#class-object-reference variable.

#normal method:
class student:
    def read(abhi):
     print("he is a python developer")

a=student()
a.read()


class student:
    def read(abhi):
     print("he is python developer")
    def write(abhi):
     print("this is abhi")

a=student()
a.read()
a.write()


class student:
    def read(abhi,x,y):
        abhi.name=x
        abhi.city=y
        print("he is python developer")

a=student()
a.read("ravi","benguluru")



class student:
    def read(abhi,x,y):
        abhi.name=x
        abhi.city=y
        print("he is python developer")
        
    def display(abhi):
        print(abhi.name,"...........",abhi.city)

s=student()
s.read("ravi","benguluru")
s.display()




#constructer:_init_
class student:
    def _init_(abhi,x,y):
        abhi.name=x
        abhi.city=y
        print("he is python developer")
        print(abhi.name,"...........",abhi.city)

s=student("ravi","benguluru")



class student:
    def _init_(self):
        self.sname="ravi"
        self.scity="benguluru"
        print("it is python developer")
    def display(self):
        print(self.sname,"...........",self.scity)

student().display()

#s=student()
#print(s.name)--object reference.
#print(student.name)--class reference.

#static var
class student:
    sname="stu_data"
    def __init__(self,stu_name,stu_id,stu_loc):
        self.name=stu_name
        self.id=stu_id
        self.loc=stu_loc
    def display(self):
        print(self.sname,"----",self.name,"----",self.id,"----",self.loc)

    

a=student("abhi","1700","guntur")
b=student("ravi","0804","benguluru")
c=student("phani","1234","tenali")

a.display()
b.display()
c.display()

 
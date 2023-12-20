#Write a program  to print sum if given number in var len argument
def add(*x):
    sum=0
    for i in x:
        sum=sum+i
        i=i+1
    print(sum)
add(10,25,35,45,55)


def f(arg1,arg2,arg3=4,arg4=8):
    print(arg1,arg2,arg3,arg4) 
f(3,5)
f(15,25,35,45)
f(11,6,arg4=1000)
f(arg4=6,arg1=7,arg2=9)

 #case-1
try:
    print("abhi")
    print(10/3)
    print("heello")
except:
    print("statement4")
    print("statement5")
finally:
    print("statement-6")
print("statement-7")  


try:

    print("abhinay")
except ZeroDivisionError:
    print("statement-4")
    print("statement-5")
finally:
    print("statement-6")
    print("statement-7") 


try:
    x=8
    print(x)
except:
    print("something went wrong")
finally:
    print("finally block is executed")  



#case-2
try:    
   print("abhi")
   print(a+b)
except NameError:
     print("variable name is not define")
finally:
     print("finally block executed") 


try:
    a=10+"abhi"
    print(a)
except TypeError:
    print("cannot add an int and a string")   
finally:
    print("finally block executed") 


try:
     a=30
     print(a.b)
except AttributeError:
    print("attribute error occured")
finally:
    print("finally block executed")   



try:
    print("hello abhinay")
    int("abc",99)
except ValueError as e:
    print("value error occcured..")  
finally:
    print("finally block exxecuted..")  



try:
     print("hiii")
     l=[i for i in range(3569000)]
     print(l)
except MemoryError:
    print("memory error occured..")  
finally:
    print("finally block excecuted...")       



# case-3
try:
    print("abhi")
    print(20/0)
    print("ravi")
except SystemError:
    print("cannot divided by zero")
    print("hello")
finally:
    print("finally block executed")
print("hi") 



try:
    print("abhi")
    a=20+"abhi"

    print("hello")
except ValueError:
    print("cannont add an int and a string")

finally:
    print("finally block executed")
print("hello")    



# case-4
try:
    print("hello abhinay")
    print(22/0)
    print("hello")
except ZeroDivisionError:
    print(10/0)
    print("cannot add an int and a string")

finally:
    print("finally block executed")
print("hello")  



try:
    print(1*90)
    print(10/0)
    print("abhi")
except ZeroDivisionError as m:
    print(10/0,"message")
    print("hii")
finally:
    print("finally block executed")

#case-5
try:
    print(2*90)
    print(1+6)
    print("hello")
except ZeroDivisionError:
    print(20/0,"message")
    print("hlo")
finally:
    print(20/0)
print("finally block executed")   




try:
    print(2*90)
    print(2+5)
    print("hello")
except ZeroDivisionError:
    print(10/0,"message",m)
    print("hlooo")
finally:
    print(10/0)
print("finally block executed") 



# #case1--exception raised at outer try
try:
    print(float("abc"))
    try:
        print("inner try block")
        print("inner try block2")
    except ZeroDivisionError:
        print("inner except block")
    finally:
        print("inner finally block")
    print("outside the inner block")
except ValueError:
    print("outer except block")
    print("outer except block2")
finally:
    print("outer finally block")
print("outside the all block")



#case-2 exception raised at outer try stm-2
try:

    print("outer try block ")
    try:
        print("inside try block")
        print(20/0)

    except ZeroDivisionError:
        print("print inner except block")
    finally:
        print("fianlly block") 
except ValueError:
    print("outer of except block")  
finally:
    print("outer finally block")
print("outer all finally block ")   





#case-3 exception raised at inner try stm-2
try:

    print("outer try block ")
 
    try:
        a=10+"hii"
        print(a)
        print("inside try block")
        
    except TypeError:
        print("print inner except block")
    finally:
        print("fianlly block")
       
except :
    print("outer of except block")
finally:
    print("outer finally block")
print("outer all finally block ") 


# case-4 exception raised at inner exception statement 3
try:
    print("hiii")
    try:
        print("inner try block")

    except ZeroDivisionError:
        print("inner except block")
        print(10/0)
    finally:
        print("inner finally block")
    print("outside the inner block")
except SyntaxError:
    print("outer except block")

finally:
    print("outer finally block")
print("outside the all block")




# case-5 exception raised at outer try and inner except statement-1,3
try:
    print(50/0)
    print("outer try block")
    try:
        print("inner try block")
    except ZeroDivisionError:
        print(20/0)
        print("inner except block")
    finally:
        print("inner finally block")
    print("outside the inner block")
except ZeroDivisionError:
    print("outer except block")
finally:
    print("outer finally block")
print("outside the all block")





# case-6 exception raised at outer try and finally block  statement-1,4
try:
    print(50/0)
    print("outer try block")
    try:
        print("inner try block")
    except ZeroDivisionError:
        print("inner except block")
    finally:
        print(10/0)
    print("outside the inner block")
except :
    print("outer except block")
finally:
    print("outer finally block")
print("outside the all block")


try:
    print("outer try block")#
    try:
        print("inner try block")#
        print(50/0)
    except ZeroDivisionError:
        print("inner except block")#
    finally:
        print("inner finally block")#
    print("outside the inner block")#
except ZeroDivisionError:
    print(40/0)
    print("outer except block")
finally:
    print("outer finally block")#
print("outside the all block")#

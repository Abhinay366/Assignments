#else block will be executed when there is no exception inside the try block
#case-1
try :
    print("abhi")
    a=3
    b="ravi"
    print(a+b)
    print(20/5)
except TypeError :
     print("typeerror is occured")
else:
    print("else")
finally:
    print("finally closing block")
    
    
#case-2-error
try  :
    print("abhi")
    a=3
    b="ravi"
    print(a+b)
    print(20/5)
except TypeError :
    a=3
    b="ravi"
    print(a+b)
    print(20/5)
    print("typeerror is occured")
else:
     print("else")
finally:
    print("finally closing block")
    
    
    
#case-3    
try :
    print("abhi")
except TypeError :
    a=3
    b="ravi"
    print(a+b)
    print(20/5)
    print("typeerror is occured")
else:
    print("else")
finally:
    print("finally closing block") 
    
    
 
#case-4-error
try :
    print("abhi")
except TypeError :
    print("typeerror is occured")
else:
    a=3
    b="ravi"
    print(a+b)
    print(20/5)
    print("else")
finally:
    print("finally closing block")  
    
    
#case-5-error
try :
    print("prathi")
except TypeError :
    print("typeerror is occured")
else:
    print("else")
finally:
    a=3
    b="ravi"
    print(a+b)
    print(20/5)
    print("finally closing block")  
    


#case-6
try :
    print("abhi")
    a=3
    b="ravi"
    print(a+b)
    print(20/5)
except TypeError :
    print("typeerror is occured")
else:
    print("else")  
    
    
#case-7
try :
    print("abhi")
    a=3
    b="ravi"
    print(a+b)
    print(20/5)
except TypeError :
    print("typeerror is occured")
finally:
  print("finally closing block") 
  
  
  
#case-8
try :
     print("abhi")
     a=3
     b="ravi"
     print(a+b)
     print(20/5)
except ValueError :
     print("valueerror is occured")
finally:
    print("finally closing block") 
 
 
 
#case-9  
try :
    print("abhi") 
finally:
  print("finally closing block")
  
  
  
#case-10
try :
    print("abhi")
except TypeError :
    a=3
    b="ravi"
    print(a+b)
    print(20/5)
    print("typeerror is occured")
else:
    a=3
    b="ravi"
    print(a+b)
    print(20/5)
    print("else")
finally:
    print("finally closing block") 
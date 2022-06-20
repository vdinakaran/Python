x=-1
try:
   if x<0:
       raise Exception("this is error")

finally:
    print("finally block excecuted")


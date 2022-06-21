try:
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    c = a/b;
    print(c)
except:
    print("can't divide by zero")
else:
    print("Hi I am else block")
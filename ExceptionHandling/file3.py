try:
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    c = a/b
    print(c)
    # Using exception object with the except statement
    #it will return the cause of an exception
except Exception as e:
    print("can't divide by zero")
    print(e)
else:
    print("Hi I am else block")
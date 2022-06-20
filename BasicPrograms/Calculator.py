num1=int(input("num1:"))
num2=int(input("num2:"))
print ("Please select the operation:")
print ("a. Add")
print ("b. Subtract")
print ("c. Multiply")
print ("d. Divide")
for i in range(4):
    choice=input("enter the choice:")
    if choice=='a':
        print(num1+num2)
    elif choice=='b':
        print(num1-num2)
    elif choice=='c':
        print(num1*num2)
    elif choice=='d':
        print(num1/num2)
    else:
        print("invalid option")


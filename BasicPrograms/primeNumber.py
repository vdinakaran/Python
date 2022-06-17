num=int(input("enter the number:"))
flag=0
if num == 0 or num == 1:
    print(num," can't be a prime or composite number ")
    exit()
for i in range(2,num):

    if num % i==0:
     flag=1

if flag==1:
    print("not prime")
else:
    print("prime")
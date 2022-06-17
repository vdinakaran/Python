num=int(input("enter the number"))
rem=0
digit=0
while (num>0):
    rem=int(num%10);
    digit=digit+rem;
    num=num/10;
print(digit)
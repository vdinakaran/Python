first=0
second=1
print(first)
print(second)
for x in range(2,4):
    fibo=first+second
    first=second
    second=fibo
    print(fibo)

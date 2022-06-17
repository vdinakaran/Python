def update(a):
    print(id(a))
    print(a)
    x=10
    print(id(x))
    print(x)

a=8
update(8)
print(id(a))
print(a)
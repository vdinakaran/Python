def oddOreven(list):
    odd=0
    even=0
    for i in range(len(list)):
        if i%2==0:
            even=even+1
        else:
            odd=odd+1
    print(odd)
    print(even)
    print("odd {},even{}".format(odd, even))
list=[12,7,9,14]
oddOreven(list)


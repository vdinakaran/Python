import sys
sys.setrecursionlimit(8)
print(sys.getrecursionlimit())
i=0
def greet():
    global i
    i = i + 1
    print("hello world",i)
    greet()


greet()


class my_class:
    x=5
p1=my_class()
print(p1.x)

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfun(self):
        print("age is ",self.age)
        print("name is ",self.name)

p2=person("kavya",18)
print(p2.name)
print(p2.age)
p2.myfun()
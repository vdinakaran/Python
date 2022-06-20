class birds:
    #class attribute
    species="birds"

    #instance attribute
    def __init__(self,name,age):
        self.name=name
        self.age=age

    #instance method
    def dance(self):
        print("{} sings".format(b1.name))
        print("{} sings".format(b2.name))

#object creation
b1=birds("peacock",5)
b2=birds("parrot",6)

#acessing instance attribute
print("name is {} and age is {}".format(b1.name,b1.age))
print("name is {} and age is {}".format(b2.name,b2.age))

#accessing class attribute
print("These are all {}".format(b1.__class__.species))
print(b1.species)

#acessing object methods
b1.dance()

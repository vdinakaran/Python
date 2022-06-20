class computer:
    def __init__(self):
        self.__maxprice=300
    def sell(self):
        print(self.__maxprice)
    def set(self,price):
        self.__maxprice=price

c=computer()
c.sell()
print("After Setting the value")
c.__maxprice=500
c.sell()
print("Set the value using setter function")
c.set(3000)
c.sell()

class sim:
    def __init__(self):
        print("sim class")
    def call(self):
        print("Sim calls")
    def data(self):
        print("Data works")

class vodaphone(sim):
    def __init__(self):
        super().__init__()
        print("vodaphone")
    def call(self):
        super().__init__()
        print("Vodaphone calls")
    def data(self):
        super().__init__()
        print("Data works")

s=sim()
v=vodaphone()
v.data()


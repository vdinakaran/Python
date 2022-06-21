class dobException(Exception):
    pass

age=int(input("enter the age:"))
try:
    if age<18:
        raise dobException("age is not valid")
except dobException as e:
    print(e)
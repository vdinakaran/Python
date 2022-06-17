from array import *

vals=array("i",[5,6,9,8])
for i in vals:
    print(i)
print(vals)
newArray=array(vals.typecode,(a for a in vals))
sq=array(vals.typecode,(a*a for a in vals))
print(sq)
print(newArray)
i=0
while(i <= len(sq)):
    print(sq[i])
    i=i+1
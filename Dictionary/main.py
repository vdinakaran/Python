thisdict={
    "name":"varshini",
    "age":18,
    "age":19, #it takes last value
    "area":"india",
    "id":1
}
#add/update details
thisdict.update({"age":22})

#remove
thisdict.pop("age")
thisdict.popitem() #removes last item
#thisdict.clear() #delete the content in dictionary
for i,j in thisdict.items():
    print(i,j)
print(thisdict.keys())
print(thisdict.values())

myfamily={
    "child1":{
        "name":"varshini",
        "age":18
    },
    "child2":{
        "name":"roshini",
        "age":14
    }
}
print(myfamily)
for i,j in myfamily.items():
    print(i,j)
print(myfamily.get("child1"))
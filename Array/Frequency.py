list=[2,3,3]
freq={}

for item in list:
    if item in freq:
        freq[item]=freq[item]+1
    else:
        freq[item]=1
for key, value in freq.items():
        print ("% d : % d"%(key, value))



punctuation="""!@#$%^&*()"""
sentence=input("enter the string:")
no_punct=""
for i in sentence:
    if i not in punctuation:
        no_punct = no_punct + i
print(no_punct)


# try:
#     file_object=open("file.txt")
#     if file_object:
#         print("file opened")
# finally:
#     file_object.close()
#
with open("file.txt") as f:
    content=f.read(10)
    print(content)
# fw=open("file.txt","a")
# fw.write(" Python has an easy syntax and user-friendly interaction.")
# fw.close()


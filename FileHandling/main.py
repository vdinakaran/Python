"""file operation can be done in following ways:
1.open
2.read/write
3.close

open
------------
open function accepts two arguments .file name and access mode
it returns the file object
syntax-file obj=open(<filename>,<access mode>)

access mode
--------------------
r-opens the file in read only mode.pointer exists at the beginning.
The file is by default open in this mode if no access mode is passed.

w-write mode.
if the file is not exist it creates one
pointer exists at the beginning

a-append mode
It opens the file in the append mode. 
The file pointer exists at the end of the previously written file if exists any.
It creates a new file if no file exists with the same name.

r+-It opens the file to read and write both. The file pointer exists at the beginning of the file.

w+-It opens the file to write and read both. 
It is different from r+ in the sense that it overwrites the previous file if one exists whereas r+ doesn't overwrite the previously written file. 
It creates a new file if no file exists.
The file pointer exists at the beginning of the file.

a+-It opens a file to append and read both.
 The file pointer remains at the end of the file if a file exists.
 It creates a new file if no file exists with the same name.
 
rb-It opens the file to read-only in binary format.
The file pointer exists at the beginning of the file.

wb-It opens the file to write only in binary format.
It overwrites the file if it exists previously or creates a new one if no file exists.
The file pointer exists at the beginning of the file.

with stmt used to close the files automatically when it done.

to read the file line by line by using a function readline() method. 
if we use the readline() method two times, then we can get the first two lines of the file

readlines() method which is used for the reading lines.
It returns the list of the lines till the end of file(EOF) is reached.

fileobj.tell()-current pointer position
fileobj.seek(10)-change the pointer position

python OS module
------------------
rename(current,old)
remove(filename)
mkdir(new)
getcwd()-current working directory
chdir(")-Changing the current working directory
os.rmdir(directory name)  -deleting directory


"""""

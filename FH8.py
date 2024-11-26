""" 
All about the seek function :
Seek function is used to change the position if the file handle or the file pointer to a 
given specified position 
File pointer s like a cursor that tells from where that data has to be read or written

Syntax:
f.seek(offset,from_what)
offset is the number of  bites to be moved
from_what is the location from where the file has to be moved
0 = move form begining 
1 = move from current location 
2 = from end 


in Python3.x and above we can seek from the begining only if the file is opened in the text 
mode 
to overcome we have to open the file in the binary mode
"""

"""
TELL function is used to tell the current position of the file  pointer 

"""

"""
writtenfile4.txt contain text:

hello

"""
f = open("writtenfile4.txt" ,"r")
print(f.tell())
print(f.read(3))
print(f.tell())
print(f.seek(0))
print(f.read())
f.close()
"""
Flush Function: It is used to forcefully write the data in the file from the buffer
"""


f = open("writtenfile5.txt","w")
f.write("This is a writtn file ")
f.flush()
f.write("SEcond line")
f.write("Third line\n ")
f.write("Fourth line ")
f.flush()
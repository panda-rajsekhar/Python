# using the r+ 
""" 
the r+ or the w+ mode can read aswell write the data of any textfile  
"""
fo = open("testfile4.txt","r+")
print(fo.write('sss'))
# in the r+ mode the cursor is in the begining of the file 
print(fo.read())
# after the alteration then upon reading the fo will give the remaining of the word of the
#text
fo.close()
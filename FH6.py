# writelines function 
f = open("writtenfile3.txt","w")
data = f.writelines(['HELLO AND WELCOME\n', 'live class\n', 'class12\t'])
print(data)
f.close()# used to close the written or the appended file 
"""
point to see is that all the data entered in the writelines function is to be in the form
of str ie enclosed in '' '' otherwiae it will give error
"""
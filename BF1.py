"""
BINARY FILES:
most of the files that are in the computer are the binaty files like:
*Image: .png,.jpg,.gif,.bmp etc
*Video:.mp4,.3gp,.mkv,.avietc
*Audio:.mp3,.waw,.mka,.aac etc
*Archive: .zip,.rar,.iso,.7z etc
*Executable: .exe,.dll,.class etc

* we cant read some of the binary files because they cant be read by the etxt eidtor

*That is because all of these file are encoded in the binary format that can be read
 only by the computer 

* there is no delimiter in a binary file 
* there is no need for the computer to convert it 
* these files are very fast 

# PICKLING : The process of the conversion of a data structure(list and dictionary ) to the 
byte stream before writing to the file 
# UNPICKLING : The process of conversion of byte stream to the original  data structure


#pickle.dump()
to write the data in the binary file we use the pickle.dump() function
the dump function will have two arguments 
syntax:
       pickle.dump(<structure>,fileobject)

#piclke.load()
its used to read the data from a file 
syntax: 
       structure = pickle.load(fileobject)
       the structure can be any sequence of python,it can be either list or dictionary 
       fileobject is the file handle 
"""
import pickle 
def write():
       f = open("binary1.dat","wb")
       l = [11,2,3,45,654,345,67,8]
       pickle.dump(l,f)
       f.close()


def read():
       f = open("binary1.dat","rb")
       data = pickle.load(f)
       print(data)
       f.close()

read()
write()


"""
The number of times the data has been dumped it has to ne loaded that number of time to see the result  

"""
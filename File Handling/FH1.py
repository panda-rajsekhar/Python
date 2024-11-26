f = open("testfile2.txt")
data = f.readlines(-4)
print(data)
print(type(data)) 
import pickle
def write():
       f = open("binary2.dat","wb")
       l = [1,2,3,4,5,6,7,8,9]
       l1= [9,8,7,6,5,4,3,2,1]
       pickle.dump(l,f)
       pickle.dump(l1,f)
       f.close()


write()
def read():
       f = open("binary2.dat","rb")
       try:
              while True:
                     data = pickle.load(f)
                     print(data)
       
       except:  f.close()

read()

"""
the procedure to read and write the data in a binary file
"""



import pickle
def write():
    f = open("binary3.dat","wb")
    while True:
        no = int(input("Rolnumber: "))
        na = input("Name: ")
        ma = float(input("Marks: "))
        rec = [no,na,ma]
        pickle.dump(rec,f)
        ch = input("insert more (Y/N):")
        if ch in "nN":
            break
    f.close()

def read():
    f = open("binary3.dat","rb")
    try:
        while True:
            data = pickle.load(f)
            print(data)


    except:
        f.close()


write()
read()

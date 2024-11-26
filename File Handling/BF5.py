import pickle
def searchrn():
    f = open("binary3.dat","rb")
    rno = int(input("Enter the Rollnumber to Seach: "))
    found = 0
    try:
        while True:
            data = pickle.load(f)
            if data[0] == rno:
                print(data)
                found = 1
            
    except:
        f.close()
    if found ==0:
        print("Record not found ...")

searchrn()
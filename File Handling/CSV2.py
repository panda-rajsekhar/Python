import csv
def search():
    fin=open("csv12.csv","r",newline='\n')
    data=csv.reader(fin)
    found=False
    print("The Details are")
    for i in data:
        if int(i[2])>10:
            found=True
            print(i[0],i[1],i[2])
    if found==False:
        print("Record not found")
    fin.close()


search()
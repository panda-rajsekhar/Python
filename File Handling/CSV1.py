"""
---------------------------------------------------------------------------------------------------------------
Csv stand for " Comman seperated values "
csv is similar to the text file in the human readable form but it is speerated by commas 
its extensively used to store the tabular data in spreadsheet or database  like that of EXEL sheets 
each record consists of fiel seperated by commas 
each line of file ia a record  
the seperator character of a scv file is called a delimiter its (,) by default in csv 
it has other delimiter like the tab('\t'),colon(:),pipe(|) and semicolon(;)
it requires a writer object and reader object
---------------------------------------------------------------------------------------------------------------
Python CSV module:
* reader = to read from csv file 
* writer = ro write form csv file 
is imported as usual 

HOW TO OPEN:
f = open("file.csv","mode")
f.close()
---------------------------------------------------------------------------------------------------------------
Writing data in csv files :
csv.writer()
object.writerow()--> writes one row
object.writerows()--> writes multiple rows
----------------------------------------------------------------------------------------------------------------
Newline Argument: 
when a csv file is formed a new line is also written which gives an empty list in the output
to avoid this situation a newline argument is added with an empty string in the file object 
----------------------------------------------------------------------------------------------------------------
All the data entered get converted to string 

----------------------------------------------------------------------------------------------------------------
to avoid the value error we use the next()function

"""
import csv
def writecsv():
    f = open("csv12.csv","w",newline= '')
    wo = csv.writer(f)
    wo.writerow(['R.NO','Name','Marks'])
    while True:
        no = int(input("Rolnumber: "))
        na = input("Name: ")
        ma = float(input("Marks: "))
        rec = [no,na,ma]
        wo.writerow(rec)
        ch = input("Enter more (Y/N)")
        if ch in "nN":
            break
    f.close()

def readcsv():
    f = open("csv12.csv","r")
    ro = csv.reader(f)
    for i in ro:
        print(i)
    f.close()

#writecsv()
readcsv()


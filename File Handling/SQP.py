""" 
Q 33 A
What is the advantage of using a csv file for permanent storage?
Write a Program in Python that defines and calls the following user 
defined functions:
(i) ADD() – To accept and add data of an employee to a CSV file 
‘record.csv’. Each record consists of a list with field elements 
as empid, name and salary to store employee id, employee 
name and employee salary respectively.
(ii) COUNTR() – To count the number of records present in the CSV 
file named ‘record.csv’
"""
# solution
import csv
def add():
    f = open("record.csv","w",newline='')
    wo = csv.writer(f)
    wo.writerow(["empid","name","salary"])
    while True:
        n = int(input("Enter Employee ID:"))
        m = input("Employee Name:")
        l = float(input("Employee Salary:"))
        rec = [n,m,l]
        wo.writerow(rec)
        ch = input("Enter More (Y/N)?")
        if ch in "nN":
            break
    f.close()

#add()
def countr():
    f = open("record.csv","r")
    ro = csv.reader(f)
    count = 0
    next(ro)
    for i in ro:
        count+=1
    print(count)
    f.close()

countr()
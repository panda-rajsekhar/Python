a = int(input("Enter the number A :"))
b = int(input("Enter the number B :"))
try:
    c = a/b
    print(c)
except ZeroDivisionError:
    print("Cant divide by zero you dumbo 8-) ")                     
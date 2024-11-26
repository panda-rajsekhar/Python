"""
with open method:
	syntax:
	with open("filename.txt","mode") as fileobject:
		print(<funciton to be applied>)

"""
with open("testfile4.txt","r") as f:
	print(f.read())


""" 
the benefit of using the with statement is that it automatically closes the file after the 
nested block of the code

it also handles all the exceptions occured before the end of the block  

"""
#!/usr/bin/env python3
import math 

#assign a value to a variable
one = '0'

# logic cotnrol statment
if '1' in one:
        print ("You maybe can code now")
else:
        print ("You are fake")

#pos vs neg
# because one = '1' is a string and NOT an int, you need to convert the string into a int using the int(x) function 
testvar = int(one)
if testvar > 0: 
	print ("You are positive...congrats")
	if testvar < 50: 
		print ("you are small")
	elif testvar > 50:
		print ("you are a big boy")	

elif testvar < 0: 
	print ("You are negative")

else:
	print ("You are nothing") 


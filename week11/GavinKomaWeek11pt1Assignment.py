import sys
import os
import numpy as np

#this will set our working directory to be able to find the necessary documents
currentpath = os.getcwd()
newpath = os.chdir('/Users/gavinkoma/Documents/bio-python/week11')
currentpath2 = os.getcwd()

#okay so our first goal is to create an array
#that is 2D of 10rows by 7columns
#numpy will assign randum numbers between 0-1
#so we will have to multiply th array by 10 to get intergers

array = np.random.rand(10,7)
array = array*10
print(array)

#okay we need to create only the interger parts of the array
#and we can do this via floor division
#which is array//1 will return only interger values

#you can also truncate and it will remove the decimal part
array_interger = array//1
print(array_interger)

#okay so now we need to make a 1d array with 12 elements
#and we need o change all numbers between 3-9 as their negative
#counterparts

darray = np.arange(12)
darray[(darray>3) & (darray<9)] = -darray[(darray>3) & (darray<9)]
print(darray)

file = open('GavinKomaWeek11pt1Assignment.txt','w')
file.write("2D array:\n")
file.write(str(array_interger))
file.write('\n\n\n' + "1D Array:\n" + str(darray))
file.close()

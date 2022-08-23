## J. Hey 9/5/2018  python 3
## program for calculating mean and standard deviation from a list of numbers

## Structure of a typical program
##   Top:  import statements
##   Middle:  function definitions,  class definitions
##   Bottom:  main program code  (does not need to be present for a file that is a module of functions and classes
##   throughtout:  comments explaining what is going on


## fyi - a triple-quoted string at the beginning of a function or a module file
## can be accessed using the help() function  - e.g. help(makesum)
## after the program has been run and the function is loaded in memory

"""
    calc_mean_var.py calculates the mean and variance of a list of numbers
"""

## we will need the math module
import math

## a function  that receives a list of numbers and returns the sum and the sum of the squared values
def makesum(nl):
    """ nl is a list of numbers.
        add up all the numbers in nl
        add up all the squares of the numbers in nl"""
    s = 0.0
    s2 = 0.0
    for i in nl:
        s += i
        s2 += i*i
    return s, s2

## MAIN PROGRAM BEGINS HERE

## ask the user how they would like to enter the numbers
## In case the user makes a mistake we can use a while loop
## This version of a while loop keep repeating until a condition is True
## The while loop will keep on repeating, forever, until the break statement is reached
## This loop prevents the program from crashing if the user does not enter an h or an f
while True:
    inputcode = input("Do you wish to enter numbers by hand (type h) or use an input file (type f)? ")
    if inputcode == 'h'  or inputcode == 'f':
        break

## The variable to contain our list of  numbers
numlist = []

## a conditional statement  (i.e. if, else)
if inputcode == 'h':
    ## another example of using a while loop with the break statement
    while True:
        ## example of using 'try' and 'except' to catch an error, and keep the program running instead of crashing
        ## if the input() statement does not work, there is an error,  trap the error to see if the loop should continue
        try:
            num = input("Enter a number (or just hit return if done): ")
            ## add the number to the end of the list.   Cast the number as a floating point value first.
            numlist.append(float(num))
        except Exception:
            if num == "":  ## empty string
                break
            else:
                print(num, " is not a number")
## else part of the conditional statement,  the program will go here if the initial condition (inputcode == 'h') is not true
else:
    fname = input("Enter the filename: ")
    f = open(fname,"r")
    ## Read all the lines of the file and put them, as a list of strings, into the variable flines
    flines = f.readlines()
    ## a 'for' loop with an iterator i that takes on the value of each item in flines
    for i in flines:
        ## i is a string,  make a floating point number from it and put that on the end of the number list
        numlist.append(float(i))

## now close the file!
    f.close()

## get the number of values in the list
n = len(numlist)

## now call the makesum() function
sumvals,sumsquarevals = makesum(numlist)

## now calculate the mean, variance and standard deviation using their conventional formulas
mean = sumvals/float(n)
variance = (sumsquarevals - pow(sumvals,2)/float(n))/float(n-1)

## to calculate the square root we must call a function that is in the math module
stdev = math.sqrt(variance)

## write the results to the screen
print ("There were ",n," numbers in the list")
print ("The mean is ",mean)
print ("The variance is ",variance)
print ("The standard deviation is ",stdev)




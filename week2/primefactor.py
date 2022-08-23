## J. Hey 9/5/2018  for python 3
## flow control example program
## prime factorization

## a function for calculating a product of a list of numbers
def calcproduct( listofnums ):
    """  calculates the product of a list of numbers """
    prod = 1
    for i in listofnums:
        prod *= i
    return prod


## main program begins here

## get a positive integer from user
n = int(input("Enter a positive integer :"))

##begin the list of prime factors
factors = []

## start with a factor of 2  (we don't count 1 as a prime factor)
i = 2

## n will change,  so save the starting value
nstart = n

## loop through until all the factors have been found
while True:
    ## no factor can be bigger than n
    if i > n:
        break
    ## check to see if i is a factor using integer division
    ## need a loop because it is possible that i is a factor multiple times
    while i * (n//i) == n:
        factors.append(i)
        ## reduce the number by the factor that was just found using integer division and assignment
        n //= i
    ## now try the next possible factor
    i += 1

##print out the results
print ("integer to factor : ",nstart)
print ("list of factors : ", factors)

## check to make sure the product of the factors is equal to the original number
print ("product of factors: ",calcproduct(factors))


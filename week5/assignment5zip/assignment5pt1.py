
#first we need to write a program
#that will load the sequences of file data for fasta

#were not going to use the actual homework assignment one
#just because its so much bigger and it would be easier for us
#to just use a smaller .fasta file

import os
import math
import random
import numpy as np
import scipy
from scipy.optimize import minimize


currentpath = os.getcwd()
newpath = os.chdir('/Users/gavinkoma/Documents/bio-python/week5')
currentpath2 = os.getcwd()

def main():
    dna1,dna2=getdnasequence()
    countsame = comparednastrings(dna1,dna2)
    countdifferent = countnonidenticalbase(dna1,dna2)
    print(countsame)
    print(countdifferent)
    pdiff = calculatepdiff(dna1,countdifferent,countsame)
    mutation = calculatemutation(pdiff)
    writetofile(countsame,countdifferent,pdiff,mutation)
    kvalloop,likelihood = bruteforcefunc(countsame,countdifferent)
    scipyfunction(countsame,countdifferent,kvalloop)
    return

def getdnasequence():
    fastafile = open(r'data_for_jukes_cantor_exercise.fa','r')
    readfile = fastafile.read()
    fastafile.close()
    print(readfile)

#okay so i need to find a way to separate the titles of the genes
#and then also compare the genes
#so i guess i really only need two lines that are just the
#gene sequences to compare, right?

    dna1seqbeginning = 'GGTACCTTTTAAGTCTC'
    dna1seqending = 'ACTGTACCTGACTGAAA'
    dna1indexbeg = readfile.find(dna1seqbeginning)
    dna1indexend = readfile.find(dna1seqending)
    dna1ending = dna1indexend+17
    dna1 = (readfile[dna1indexbeg:dna1ending])

    dna2seqbeginning = 'GCTTCGTCGCACT'
    dna2seqending = 'CTGTCTG-AT'
    dna2indexbeg =  readfile.find(dna2seqbeginning)
    dna2indexend = readfile.find(dna2seqending)
    dna2ending = dna2indexend+10
    dna2 = (readfile[dna2indexbeg:dna2ending])

    e = '\n'

    print('These are the two dna sequences:',e,dna1,e,dna2)

    return(dna1,dna2)
#okay so i have the two sequences without names and now
#i need to count/compare how many idential bases there are
#in these two sequences

def comparednastrings(dna1,dna2):
    countsame = 0
    if len(dna1) != len(dna2):
        print('Length of strings do not match.')
    for c in range(len(dna1)):
        if dna1[c] == dna2[c]:
            if not (dna1[c] == '-' or dna2[c] == '-'):
                countsame = countsame + 1
    return(countsame)

def countnonidenticalbase(dna1,dna2):
    countdifferent = 0
    if len(dna1) != len(dna2):
        print('Length of strings do not match.')
    for c in range(len(dna1)):
        if dna1[c] != dna2[c]:
            if not (dna1[c] == '-' or dna2[c] == '-'):
                countdifferent = countdifferent +1
    return(countdifferent)

def calculatepdiff(dna1,countdifferent,countsame):
    print(int(len(dna1)))
    pdiff = countdifferent/(countdifferent+countsame)
    print(pdiff)
    return(pdiff)

def calculatemutation(pdiff):
    mutation = (-0.75)*math.log((1-((4*pdiff)/3)))
    print(mutation)
    return(mutation)

def writetofile(countsame, countdifferent, pdiff, mutation):
    result = open('assignment5part1results.txt','w')
    e = '\n'
    line1 = 'The value of identical bases (S) is: ' + str(countsame)
    line2 = 'The value of different bases (D) is: ' + str(countdifferent)
    line3 = 'The porportion of different bases (p) is: ' + str(pdiff)
    line4 = 'The estimate of the number of mutations per site (K") is: ' + str(mutation)
    line5 = 'The brute force calculation to determine the log likelihood returned the following details: '
    result.writelines([line1,e,line2,e,line3,e,line4,e,e,line5,e])
    return()


#lets make another section for the other half of part1;
#i dont like the idea of continuing it in the main function; we can call it later

#nevermind, i cant do that because countdifferent and countsame are made in the main function
#and im not sure how to pass something created in one function to another function
#without making it global?


def bruteforcefunc(countsame,countdifferent):
    def likelihood(countsame, countdifferent, kval):
        #probdiffbase = (0.75)*(1-(math.exp((-4*kval)/3)))
        probdiffbase = (0.75)*(1 - (math.exp((-4*kval)/3)))
        #loglikelihood = (countdifferent)*(math.log(probdiffbase))+((countsame)*math.log(1-probdiffbase))
        #we are returning the negative log so that instead of minimization it is actually the maximization
        loglikefunc = -((countdifferent)*(math.log(probdiffbase))) + ((countsame)*math.log(1-probdiffbase))
        return loglikefunc

#okay so if we define our functions previously as functions of each other,then we can just reference
#the function as a whole later without retyping everything

#start with an empty list that we will append to, the values of k0 and k1 will act as conditions
#for the loop that we will have to use basically k0 will be the 0 index (our first index for the value list)
#k1 will be the 1 index (second entry for the value list)
    likeval = []
    k0 = 0.001
    likeval.append(likelihood(countsame,countdifferent,k0))
    k1 = 0.002
    likeval.append(likelihood(countsame,countdifferent,k1))

#our loop states that while [i] is greater than [j] (the previous index is greater than the next index)
#to continue looping. our next kval is calculated using the predefined liklihood function that utilizes
#values S, D, and pdk. It will then print the kvalloop and the kvall number and then append this value
#as our newest likeval value the loop will progress in 0.01 increments and continue
#until liveval[i]<likeval[j]
    kvalloop = 0.003
    i = 0
    j = 1
    while likeval[i]>likeval[j]:
        nextkval = likelihood(countsame,countdifferent,kvalloop)
        #print(kvalloop,nextkval)
        likeval.append(nextkval)
        #+= is also a valid indicator to use for the additive function
        kvalloop = kvalloop + 0.001
        i = i + 1
        j = j + 1

    print('Loop: ' + str(kvalloop) + ' Indicated value: ' + str(likeval[j]))
    result = open('assignment5part1results.txt','a')
    linebrute = 'Loop: ' + str(kvalloop-0.001) + ' Indicated value: ' + str(likeval[-1])
    e = '\n'
    result.writelines([linebrute,e,e])
    return(kvalloop, likelihood)

def scipyfunction(countsame,countdifferent,kvalloop):
    #okay i couldnt figure out how to pass just the likelihood function again from the previous
    #function because the functions are nested in the loop and im not sure how to separate them
    #so instead i've just pasted it again into this section because likelihood will need to be
    #redefined to utilize the scipy function
    def likelihood(countsame, countdifferent, kval):
        #probdiffbase = (0.75)*(1-(math.exp((-4*kval)/3)))
        probdiffbase = (0.75)*(1 - (math.exp((-4*kval)/3)))
        #loglikelihood = (countdifferent)*(math.log(probdiffbase))+((countsame)*math.log(1-probdiffbase))
        #we are returning the negative log so that instead of minimization it is actually the maximization
        loglikefunc = -(countdifferent)*(math.log(probdiffbase)) + ((countsame)*math.log(1-probdiffbase))
        return loglikefunc

    scipyresult = scipy.optimize.minimize_scalar(lambda k: likelihood(countsame,countdifferent,kvalloop))
    print(scipyresult)

    linescipy = 'By using the scipy.optimize.minimize_scalar() function, our calculated likelihood value is:'
    e = '\n'

    result = open('assignment5part1results.txt','a')
    result.writelines([linescipy, e, str(scipyresult)])
    return

    linescipy = str(scipyresult)


main()




#

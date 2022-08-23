##
#start by importing the necessary modules
#i also always need to change the working directory or else i cant ever call
#on the files that i need

import math
import os
import csv
import numpy as np

#here we change the directory so i can access the files for the python script
currentpath = os.getcwd()
newpath = os.chdir('/Users/gavinkoma/Documents/bio-python/week6')
currentpath2 = os.getcwd()

#this code was given to use in distance_matrix_getting_started.py
def makeemptymatrix(n):
    m = []
    for i in range(n):
        temprow = []
        for j in range(n):
            temprow.append(0)
        m.append(temprow)
        #print(m)
    return(m)

#just this is a copy & paste from my part1 homework assignment. The only difference
#is that the code has been altered to use seq1 and seq2 instead of what i originally wrote
#(dna1 & dna2)
def calculatep(seq1,seq2):
    countsame = 0
    countdifferent = 0
    if len(seq1) != len(seq2):
        print('Length of strings do not match.')
    for c in range(len(seq1)):
        if seq1[c] == seq2[c]:
            if not (seq1[c] == '-' or seq2[c] == '-'):
                countsame = countsame + 1
    for c in range(len(seq1)):
        if seq1[c] != seq2[c]:
            if not (seq1[c] == '-' or seq2[c] == '-'):
                countdifferent = countdifferent +1

    p = countdifferent/(countdifferent+countsame)
    return(p)


def calculateKfromp(p):
    #this is also just a copy and paste from my previous part1 of the assignment5
    K = (-0.75)*math.log((1-((4*p)/3)))
    return(K)


def mainmatrix():
    # """
    #     write a function that reads the file and loads
    #     the species names into a list of strings
    #     and loads the sequences into a list of strings
    # """
    fastafile = open('Myotis_aligned.fa','r')
    fastadata = fastafile.readlines()
    fastafile.close()
    #also this method of opening the lines makes far more sense than how i was
    #previously opening fasta files

    #okay so now we need empy matrix for names, sequences1 and sequences2
    #these empty matrices will allow for our comparisons between sequences
    names = []
    sequences = []
    fastadata2 = []

    for i in range(len(fastadata)):
        #so here wer
        removebreak = fastadata[i].replace('\n', '')
        fastadata2.append(removebreak)

        #so here we determine if the values are positive or negative
        #the names are on all odd numbers while the sequences are all on even numbers
        #by appending each line based on which they are, we can make separate lists
        #for each of them
        if i%2 == 0:
            #here we append names
            names.append(fastadata2[i])
            #here we append sequence
        else:
            sequences.append(fastadata2[i])

#now we set the boundary length for the matrices
#these are determined by the length of each list created
    n = len(names)
    #print(n)
    m = makeemptymatrix(n)
    #print(m)

    #we should get our index values as well for filling our empty matrix
    index_vals = [num for num in range(0,len(names))]
    #print(index_vals)


#okay so finally we need to match matrices for proper analysis; we want to consider
#the index of the values in each & count the iterable
#so here we have values a,b in the index, we are looping & counting a in the
#index_vals and for be we are listing the values in the entire index
    combos = [(a,b) for index, a in enumerate(index_vals) for b in index_vals[index+1:]]
    #print(combos)

#now we also need to match the pairs to create our matrix
    for values in range(len(combos)):
        #here we first need to designate the row of the matrix and the columns
        row = combos[values][0]
        col = combos[values][1]

        #now we need to fill the rows and the columns with our sequence fastadata
        #seq1 will be row and seq2 will be col, but we can use either for this
        #and it should be the same answer
        seq1 = sequences[row]
        seq2 = sequences[col]

        #we are redefining p and K to use K as a value for our distance matrix
        #p is references in calculatep function and k uses the p from calculatep
        #in the calculateKfromp function
        p = calculatep(seq1,seq2)
        K = calculateKfromp(p)

        #finally our matrix is defined and filled here
        #we use empty matrix m filled with rows and columns
        #which wer previously filled by seq1 and seq2 comparisons and should
        #equal our value K
        m[col][row] = K
        m[row][row] = K

    #okay so now that we have the pairings for our files
    #we need to use the pairings for our matrix and these indices
    #will basically tell the computer where the values need to go
    for c in range(len(names)):
        specieindex = names[c]
        m[c].insert(0,specieindex)

    names.insert(0,"")
    m.insert(0,names)
    #print(m)

#here is how we write the data to the .csv file, i cant figure out how
#to make this into a .txt
    with open("distancematrixresult.csv",'w',newline="") as q:
        write = csv.writer(q)
        write.writerows(m)
        matrix = m
        low = np.amin(matrix)

    return matrix, names


##################
##################
##################
##################
##################
##################
##################

def min_cell(matrix):

    table = matrix

    m_np = np.array(table).astype(float)

    low = np.amin(m_np)
    d2 = low/2
    #print(low)
    res = np.where(m_np == low)
    #print(res)
    x, y = res
    print(x,y)
    return(x,y,m_np)


def main():
    matrix, names = mainmatrix()
    min_cell(matrix)






main()

#

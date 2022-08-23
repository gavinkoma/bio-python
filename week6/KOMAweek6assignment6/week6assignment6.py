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
        m[row][col] = K

    #okay so now that we have the pairings for our files
    #we need to use the pairings for our matrix and these indices
    #will basically tell the computer where the values need to go
    #for c in range(len(names)):
        #specieindex = names[c]
        #m[c].insert(0,specieindex)

    #names.insert(0,"")
    #m.insert(0,names)
    #print(m)

#here is how we write the data to the .csv file, i cant figure out how
#to make this into a .txt
    with open("week6assignment6distancematrix",'w',newline="") as q:
        write = csv.writer(q)
        write.writerows(m)

    matrix = m

    return matrix, names

#################################
#################################
#################################
#################################
#################################
#################################
#################################
#everything below this line is used for week6 assignment#
#################################
#################################
#################################
#################################
#################################
#################################
#################################

# def lowestcell(m):
#     table = m
#     #print(type(m))
#     #print(type(table))
#     m_np = np.array(table).astype(float)
#     #print(type(m_np))
#     low = np.amin(m_np)
#     d2 = low/2
#     #print(low)
#     res = np.where(m_np == low)
#     #print(res)
#     x, y = res
#     print(x,y)
#     return(x,y,m_np)

def min_cell(matrix):

#this part is similar to the newicksim.py code that picks two random numbers and compares them
#however, this is differnt, basically were starting with a massive number as a
#comparison for our values here, in this case were using infinity as a float

    mincomparison = float("inf")

    minrow, mincol = -1, -1

    #ok so now were going to go through all of the values of the row and look
    #for the smallest of the values; this will enumerate every row of our matrix
    for i, row in enumerate(matrix):
        #this will now go through the other values of the matrix as well
        #our row is actually the column
        for j, val in enumerate(row):
            #so now were comparing our i value and our j value and just double checking
            #that the values arent zero. if the values are 0 then the code wont
            #continue because 0 would just be a factor of the identity matrix so
            #ignore zeroes
            if mincomparison > val and val > 0.0:
                #here i need to assign values to that will be continuously referenced
                #and then allow for the mincomparison (which is the smallest distance
                #in our distance matrix), and the coordinates the minrow and the mincol
                mincomparison = val
                minrow = i
                mincol = j
    # print(type(min_num))
    # print(type(min_col))
    # print(type(min_row))
    # print(type(matrix))
    return mincomparison, minrow, mincol


#all the code below here was me using numpyarray as the matrix but i couldnt properly
#index things as the code progressed so instead this is just commented out and
#the new approach (above) just indexes a list of lists which was easier than numpy
#mostly because im not sure how to use numpy properly

# def join_labels(names, x, y):
#     # Swap if the indices are not ordered
#     labels = names
#     print(labels[int(x)])
#     print(labels[int(y)])
#
#     labels[int(x)] = "(" + labels[int(x)] + "," + labels[int(y)] + ")"
#     print(labels)
#     print(labels[int(x)])
#
#     del labels[int(y)]

# join_table:
# #   Joins the entries of a table on the cell (a, b) by averaging their data entries
# def join_table(m_np, x, y):
#     # For the lower index, reconstruct the entire row (A, i), where i < A
#     row = []
#     updatem_np = np.array(m_np).astype(int)
#     for i in range(0, x):
#         row.append((updatem_np[x][i] + updatem_np[y][i])/2)
#     updatem_np[a] = row


def buildnewnode(node1, node2,mn):

#this code is directly from the newicksim.py code file
#but i added the mn/2 value to include the distances for the phylo
#tree that will output

    """ build a newickformat node by combining node1 and node2
    node1 and node2 are strings.

    From newicksim.py """

    return "(" + node1 + "," + node2 + "):" + str(mn/2)

    #mn/2 is the distance for the nodes to be included on the tree



#okay here is the clunky messy hard part of getting the newick string to output properly
def newick(matrix, names):

#were calling our matrix from last week and just using the distances here
#this while function says to keep iterating until there is only a 1x1 matrix left
#this is to make sure weve traced all species back to their origin for the species

    while len(matrix) > 1:

#call the min number, min rowvalue, and min column value from our minimum cell matrix
#this will continue over and overagain and rewriting which values are for the min row/min col
        mn, mr, mc = min_cell(matrix)

        #below will reference the new node function after each iteration, this is how
        #we will continue to build new nodes after each iteration
        #until 1x1 matrix

        names.append(buildnewnode(names[mr], names[mc], mn))

        #we next remove each row after its been used to make sure that the code
        #does not consider new values as old values (basically we dont want to
        #use the same name multiple times)

        names.remove(names[mr])
        names.remove(names[mc])

        #this creates a new matrix that is necessary for the newick func`
        #the newrow will be referenced later but continuosly appended
        new_row = []

        #pdb.set_trace()
        # Loop over every element in one row of the dist_matrix; the one
        # at min_row. eg this is:

        ''' (Pdb) dist_matrix[min_row]
[0.2606454532514589, 0.2282574786568678, 0.23213020884654634, 0.21722496943728203, 0.21488487393509928, 0.2290362371633863, 0.22784670479666036, 0.3027841944605626, 0.23381332337749627, 0.23862103214818559, 0.235012364400269, 0.2532318838270524, 0.2581661121505844, 0.23022765917723978, 0.23862103214818559, 0.2532318838270524, 0.23381332337749627, 0.23982779025246106, 0.2290362371633863, 0.2362133254254994, 0.24955239975041155, 0.2266590560924271, 0.24710940084768174, 0.25200338232387376, 0.24832990559221335, 0.2422471471891231, 0.2326161962278796, 0.255694940227945, 0.24345975860930205, 0.23862103214818559, 0.22784670479666036, 0.235012364400269, 0.23862103214818559, 0.23741621261198034, 0.2532318838270524, 0.2833362595198107, 0.23022765917723978, 0.2125520571243049, 0.29885405446289537, 0.2102264738656188, 0.21839776091941906, 0.23022765917723978, 0.25200338232387376, 0.22192717919747845, 0.25692950840794637, 0.2631330177209544, 0.2362133254254994, 0.23381332337749627, 0.2362133254254994, 0.24589087905243034, 0.2581661121505844, 0.2618882041571811, 0.24467433377352937, 0.23381332337749627, 0.24467433377352937, 0.25446240092014744, 0.2631330177209544, 0.2422471471891231, 0.007936581997902729, 0.11342322729294264, 0.11036823325221577, 0.2248434766718579, 0.22547328509443793, 0.2422471471891231, 0.2362133254254994, 0.24345975860930205, 0.25200338232387376, 0.2422471471891231, 0.2410364931732173, 0.2731666121805865, 0.29494440182149556, 0.29494440182149556, 6000000.0, 6000000.0, 6000000.0]
(Pdb) len(dist_matrix[min_row])
75
'''
# okay so we need to keep iterating through our matrices
# so this first part basically is just making sure that were not
# approaching zero for any of our indexing
# this is just a safe guard
# so for x,y in every single index for the matrix

        for i, dist_row in enumerate(matrix[mr]):
            value1 = matrix[mc][i]
            #this is a safe guard to make sure were not using the values of
            #0 for our min value of our distance matrix
            #this makes sure that our dist_row does not equal zero and the index
            #value of our matrix is not 0
            if dist_row != 0.0 and value1 != 0.0:
                #this calculates the new values that will be appended to the new row
                #this is also included in the power point slides give because the new
                #row A+B needs to be (A+B)/2
                value2 = (dist_row+value1)/2
                #we now repleace all the values given here with the new mean value of the matrix
                new_row.append(value2)

        for j, row in enumerate(matrix):
            #alright so now we need to remove the values that we just averaged and m
            #made a new row/col with
    #        print(str(i)+"index")
    #        here we are removing the indexed value of matrix[i] from the row
            matrix[j].pop(mr)
            #here we are removing the column value at matrix[j]
            #when i didnt have mc-1 the indexing would regularly go out of the matrix
            #and not continue
            #genuinely not sure why we needed to include this, but a similar asking
            #was posted on stack overflow and it included this mc-1
            matrix[j].pop(mc-1)

        #i originally had these values in nested arguments to just not be repititive
        #but it wasnt working

        #we are now assigning the row of matrix at mr to value m
        m = matrix[mr]
        #here we are assinging column value at mc of matrix
        n = matrix[mc]
        #now below removes the entire row/column from our matrix.
        #the above commands only remove the indexed value from our matrix
        #this actually removes the line of values so were not having
        #repeat values in our matrix that might be referenced at a later date
        matrix.remove(m)
        matrix.remove(n)

#okay so weve averaged the row and removed the column and rows
#here were going to replace our value with 0 at the orignal location of where
#our min distance was
#we have k,row in the entire matrix
#the col value of newrow at index k
#is appended the column to our matrix at [k]
        for valuek, rowvalue in enumerate(matrix):
            colulmnvalue = new_row[valuek]
            matrix[valuek].append(colulmnvalue)

#at the very end of our code, well want to appende
#the rest of our calculated matrix to our matrix to complete all values
#and to make sure were iterating through every single distance value
        new_row.append(0)
        matrix.append(new_row)

        #return the names for the newick code string
    return names


def main():
    #this is function is entirely from last week,
    #it calculated our distance matrix that we are using
    #for this week's newick code
    matrix, names = mainmatrix()

    #we return our names from our newick function
    names = newick(matrix, names)
    #print(names)

#i tried to have the newick file write as it was open
#but when i do that, commas get inserted between every single character and im
#not entirely sure why that is
#but it works fine when just writing it as a string
#i left the code commented below, it worked fine when writing my matrix
    #
    # with open("week6assignment6distancematrixopen",'w',newline="") as q:
    #     write = csv.writer(q)
    #     write.write(str(names))

    print("newickstring:" + str(names))
    final_newick_file = open("week6assignment6newick.txt","w")
    final_newick_file.write(str(names))
    final_newick_file.close()


#the last thing is that it runs fine but i cannot get the code to not output
#the first bracket and the first comma
#if you copy and paste all values into the newick text box
#without the starting bracket and without the end bracket
#and both the start & finish apostraphe, then the newick
#file outputs a phylogenetic tree with the branch lengths overlayed on top


#run our main function
#please work
main()

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
newpath = os.chdir('/Users/gavinkoma/Documents/bio-python/week5')
currentpath2 = os.getcwd()

#this code was given to use in distance_matrix_getting_started.py
def makeemptymatrix(n):
    m = []
    for i in range(n):
        temprow = []
        for j in range(n):
            temprow.append(0)
        m.append(temprow)
        print(m)
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
    print(combos)

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

    #okay so now that we have the pairings for our files
    #we need to use the pairings for our matrix and these indices
    #will basically tell the computer where the values need to go
    for c in range(len(names)):
        specieindex = names[c]
        m[c].insert(0,specieindex)

    names.insert(0,"")
    m.insert(0,names)
    print(m)

#here is how we write the data to the .csv file, i cant figure out how
#to make this into a .txt
    with open("distancematrixresult.csv",'w',newline="") as q:
        write = csv.writer(q)
        write.writerows(m)

    return m, names


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

def min_cell(m):

    ''' this function finds the minimum cells in the distance matrix '''
    matrix = m
    low = np.amin(matrix)
    # min_num = float(np.inf) # start with infinity aka a really big number
    # min_row, min_col = -1, -1
    #
    # # Search all the cells to find smallest number
    # for i, row in enumerate(matrix):
    #     for j, val in enumerate(row):
    #         if min_num > val and val > 0.0:
    #             min_num = float(val)
    #             min_row = i
    #             min_col = j
    #
    # print(min_col)
    # return min_num, min_row, min_col


def buildnewnode(node1,node2):
    return "(" + node1 + "," + node2 + ")"

def newick(m_np, names):

    dist_matrix = m_np.tolist()
    print(type(dist_matrix))
    print(dist_matrix)

    species_list= names
    ''' this function creates the newick tree string.

        the function requires the distance matrix and the
        original species list.'''

    while len(dist_matrix) > 1: # iterate until all nodes are combined

        # Find min cell in distance matrix
        min_num, min_row, min_col = min_cell(dist_matrix)

        # Identify the nodes that correspond to the min cell
        node1 = species_list[min_row]
        node2 = species_list[min_col]

        # Remove those nodes
        species_list.remove(node1)
        species_list.remove(node2)

        # Build a new node: (node1, node2)
        species_list.append(buildnewnode(node1,node2))

        # Calculate new (averaged) values and insert it into an empty matrix
        matrix = []

        print(min_col)
        #pdb.set_trace()
        # Loop over every element in one row of the dist_matrix; the one
        # at min_row. eg this is:
        ''' (Pdb) dist_matrix[min_row]
[0.2606454532514589, 0.2282574786568678, 0.23213020884654634, 0.21722496943728203, 0.21488487393509928, 0.2290362371633863, 0.22784670479666036, 0.3027841944605626, 0.23381332337749627, 0.23862103214818559, 0.235012364400269, 0.2532318838270524, 0.2581661121505844, 0.23022765917723978, 0.23862103214818559, 0.2532318838270524, 0.23381332337749627, 0.23982779025246106, 0.2290362371633863, 0.2362133254254994, 0.24955239975041155, 0.2266590560924271, 0.24710940084768174, 0.25200338232387376, 0.24832990559221335, 0.2422471471891231, 0.2326161962278796, 0.255694940227945, 0.24345975860930205, 0.23862103214818559, 0.22784670479666036, 0.235012364400269, 0.23862103214818559, 0.23741621261198034, 0.2532318838270524, 0.2833362595198107, 0.23022765917723978, 0.2125520571243049, 0.29885405446289537, 0.2102264738656188, 0.21839776091941906, 0.23022765917723978, 0.25200338232387376, 0.22192717919747845, 0.25692950840794637, 0.2631330177209544, 0.2362133254254994, 0.23381332337749627, 0.2362133254254994, 0.24589087905243034, 0.2581661121505844, 0.2618882041571811, 0.24467433377352937, 0.23381332337749627, 0.24467433377352937, 0.25446240092014744, 0.2631330177209544, 0.2422471471891231, 0.007936581997902729, 0.11342322729294264, 0.11036823325221577, 0.2248434766718579, 0.22547328509443793, 0.2422471471891231, 0.2362133254254994, 0.24345975860930205, 0.25200338232387376, 0.2422471471891231, 0.2410364931732173, 0.2731666121805865, 0.29494440182149556, 0.29494440182149556, 6000000.0, 6000000.0, 6000000.0]
(Pdb) len(dist_matrix[min_row])
75
'''
        for i, val in enumerate(dist_matrix[min_row]):
            #pdb.set_trace()
            print("min_col is %d i is %d and len(distmatrix) is %d and len(distmatrix[min_col] is %d)" % (min_col,i,len(dist_matrix),len(dist_matrix[min_col])) )
            val2 = dist_matrix[min_col][i]
            if val != 0.0 and val2 != 0.0:
                new_col = (val + val2) / 2
                matrix.append(new_col)

        # Remove used values in the distance matrix for each row at index x
        for x, row in enumerate(dist_matrix):
            dist_matrix[x].pop(min_row)
            dist_matrix[x].pop(min_col-1)

        # Delete used rows in the distance matrix
        nix1 = dist_matrix[min_row]
        nix2 = dist_matrix[min_col]
        dist_matrix.remove(nix1)
        dist_matrix.remove(nix2)

        # Add averaged column from matrix to distance matrix
        for j, row in enumerate(dist_matrix):
            col = matrix[j]
            dist_matrix[j].append(col)

        # Add rest of matrix to distance matrix
        matrix.append(0)
        dist_matrix.append(matrix)

    return species_list


def main():
    m,names = mainmatrix()
    # x,y,m_np = lowestcell(m)
    mn,mr,mc=min_cell(m)
    print("Min num: %d Min row %d Min col %d" % (mn,mr,mc) )
    print(x,y)
    newick(m_np, names)

    # join_labels(names, x, y)




main()

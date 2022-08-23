#modules
#from Bio import SeqIO
import collections
import sys
import os

#this will set our working directory to be able to find the necessary documents
currentpath = os.getcwd()
newpath = os.chdir('/Users/gavinkoma/Documents/bio-python/week9')
currentpath2 = os.getcwd()


#part1
with open('genelist.txt','r') as f:
    content = f.read().splitlines()
    species_array = []
    species_genes = []
    for line in content:
        if line.startswith('Species_'):
            if species_genes:
                species_array.append(species_genes)
            species_genes = []
        species_genes.append(line)
    species_array.append(species_genes)

    # print (len(species_array))
    # print(species_array)

#okay so now we have to go through and count them;
#they are currently as an array of different species and
#the genes associated

total = []
for l in range(len(species_array)):
    num = len(species_array[l])-1
    total.append(num)
#we subtract - 1 to not count the species name
# print(total)

#okay so weve done the count of each species; we need to now
#take the count of unique gene specienames for each species
#but am i cross comparing these or are these just the same within
#its own list?

unique_gene = []
for s in range(len(species_array)):
    unique_gene_set = set(species_array[s][1:])
    unique_len = len(unique_gene_set)
    unique_gene.append(unique_len)
# print(unique_gene)
    # unique = len(species_array[s])
    # unique_gene.append(unique)
    #
    # print(unique_gene)

#okay so now we need to get the number of gene specienames
#that are unique for species[i] that are also among the specienames
#for species[j], do this for all pairs and print out the values in
#a 14x14 table

#then have a program generate a matrix with 14 rows and 14 columns
#with all the pairs and write it to a file

#okay so this is going to go through and make combos
#of the indexes for the species
iterate = [number for number in range(0,len(species_array))]
# print(len(iterate))
combo = [(a,b) for index, a in enumerate(iterate) for b in iterate]
# print(len(combo))

#and now we need to go through and compare them
#and see if they are the same or not in any of them
#we can do this with an = sign and append
#the value as a new overwritten value

# create a zero matrix 2d list 14x14
matrix = []
n = 14
for vali in range(n):
    temporary = []
    for valj in range(n):
        temporary.append(0)
    matrix.append(temporary)

# loop over all 14 species, and then within, loop over all 14 again, place in matrix.
for row in range(14):
    for col in range(14):
        #species of row
        speciesi = species_array[row]

        #species of column
        speciesj = species_array[col]

        #start value is 0 because no matches atm
        samecount = 0

        #compare them
        for val in speciesi:
            if val in speciesj:
                samecount += 1

        #set values in the matrix; this is kind of like the distance matrix we did
        #errr well technically it was an identity matrix but idk maybe im thinking wrong
        matrix[row][col] = samecount
        matrix[col][row] = samecount

#print(matrix)


#okay time to format the final matrix for submission
#im currently getting an extra set of species# and i dont know why
#'Species_0','Species_1','Species_2','Species_3','Species_4','Species_5','Species_6','Species_7','Species_8','Species_9','Species_10','Species_11','Species_12','Species_13'
#so i was getting an extra row here before because i was not only adding the numbers via index value of length
#but i was also just straight up inserting a whole row

#here is the empty we will be appending to
specienames = []

#add name values based on the length of the specie array
#this will give us 14 values (from 0-13)
for i in range(len(species_array)):
    specieval = 'Species_' + str(i) #we say 'Specie_' because it matches the orignal names given to us
    specienames.append(specieval) #append these values to the names (empty)
    matrix[i].insert(0, specieval) #insert them

specienames.insert(0,'') #insert an empty space at the very first index so that our naming is correct
matrix.insert(0, specienames) #insert names

#found this on stackoverflow, not really sure why it works; I was having trouble
#introducing the names values at the start of every string
#i couldnt get the vertical column basically
#found it here: https://stackoverflow.com/questions/13214809/pretty-print-2d-list
mresult = ('\n'.join([''.join(['{:12}'.format(item) for item in row])
    for row in matrix]))



totalcountresult = 'The total number of genes for each species is: ' + '\n' + str(total)
# print(totalcountresult)
uniquegeneresult = 'The number of unique genes for each species is: ' + '\n' + str(unique_gene)
# print(uniquegeneresult)

file = open('KomaAssignment9pt1output.txt', 'w')
file.write(totalcountresult +'\n\n'+ uniquegeneresult +'\n\n'+ 'The combination of unique genes for each pair of species:'+'\n'+ mresult)
file.close()

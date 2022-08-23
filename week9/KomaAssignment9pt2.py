#import modules needed

from Bio import SeqIO
import collections
import sys
import os

#this will set our working directory to be able to find the necessary documents
currentpath = os.getcwd()
newpath = os.chdir('/Users/gavinkoma/Documents/bio-python/week9')
currentpath2 = os.getcwd()

#okay so first we need to start by reading the fasta file

#empty list of accesssion numbers
#empty list of sp names

myotisacc = []  # list of accession nums
myotissp = []  # list of species names

for sequencerecord in SeqIO.parse('Myotis_aligned.fa', 'fasta'):
    #this was on the biopython website; needed some help with figuring it out
    #this is our record numbers
    sr = sequencerecord.id.split(".", 1)[-2]
    #now were adding the accession numbers to the list
    myotisacc.append(sr)
    #and this adds the species to the list
    myotissp.append(sequencerecord.id.split("_",1)[1])

#it prints 75 which is good; should be 75
#we have 75 entries in our myotisaligned file
#print(len(myotisacc))


def myhash(accession_num):
    #ok so this assigns a value for alpha that is 1-26 of each letter
    #of the alphabet that we use that appears in the accession number
    #in our list
    alphaval = [str(ord(x) - 75) for x in accession_num.lower() if x >= 'a' and x <= 'z']

    #ok so now our alpha values go through multiplications to differentiate
    #them from each other; this just helps to create random values that will
    #be later used
    hash_num = int(''.join(alphaval)) + int(accession_num[2])*2 + int(accession_num[3])*3 + int(accession_num[4])*4 + int(accession_num[5:])*5

    return int(hash_num)

#empty list for the hash numbers
hash_numbers = []

#placeholders, increased to 100000 to account for all numbers
myotissequences = [0 for num in range(int(10000))]


#here we have a for loop to index
#the i is the index value while accession is the accession number
#we need this to reference for printing
for i,accession in enumerate(myotisacc):
    myotissequences[myhash(accession)] = myotissp[i]

    #list of hash numbers to reference
    hash_numbers.append(myhash(accession))

    #while the file is open, append all output values to the file
    #this is output file for assignment
    with open("KomaAssignment9pt2output.txt", "a") as file:
        file.write('Accession #: '+ str(accession) + '\nSpecies: ' + str(myotissequences[myhash(accession)]) + '\nHash #: ' + str(myhash(accession)) + '\n\n')

#so im thinking of this in terms of sets
#like it wouldnt make sense for values to have repeats?
#if they repeat youd be referencing more than one thing at a time so
#itd be important to make sure that each value only occurs once & we should check this

#originally was thinking that this would be doable if i put each thing in a set
#but i couldnt get the sets to work or for the code to tell me what i wanted it to
#so instead weve just got a duplicate counter and if it returns a value that is
#nonzero then that value indicates how many duplicates there are here

#were doing this with a dictionary actually because i dont entirely understand sets
hashnumberdup = {}
duplicates = []


for val in hash_numbers:
    if val not in hashnumberdup:
        #so each hash number has a value of 1 when it first gets into the dict
        hashnumberdup[val] = 1

    else:
        #every time it gets added after that, the number will increase
        #so this is how well check if there are duplicates
        if hashnumberdup[val] == 1:
            duplicates.append(val)
        hashnumberdup[val] = 1 + val

#just to double check that there are no repeats
print(len(duplicates))

#okay first import all libraries and modules that you might need

import os
import sys
import subprocess
from Bio import Entrez
from Bio import SeqIO
from Bio import AlignIO
from Bio.Align.Applications import MuscleCommandline
from Bio import Phylo
from Bio.Phylo.Applications import PhymlCommandline

currentpath = os.getcwd()
newpath = os.chdir('/Users/gavinkoma/Documents/bio-python/week7/submission')
currentpath2 = os.getcwd()

my_email = "tug44382@temple.edu"

#this is a list of the asseccesion numbers for the tree
list_id = ['D37816', 'D37817.1', 'L00608.1', 'X60725','D37815.1', 'D37813.1', 'D37811.1', 'X69494.1','X69496.1', 'D37812.1', 'FJ374696.1']

#this will search through ncbi for the above sequences
my_handle = Entrez.efetch(db="nucleotide", id=list_id,rettype="gb",retmode = "text",email=my_email)

#we can use seq.ioparse to make a list of the Sequences
#this will also make a list that contains the lengths of the sequences for us
seq_records = []
sequences = []
length = []

#this for loop will append sequence records to seq_records
#sequences to Sequences
#and length to our empty length matrix
for sr in SeqIO.parse(my_handle, "genbank"):
    seq_records.append(sr)
    sequences.append(sr.seq)
    l = len(sr.seq)
    #print(l)
    length.append(l)

#close the file after were done
#couldnt figure out how to do this with a with open function
my_handle.close()

#okay so here we want to write our results to a text file that we can use later
#this will be referenced again when we make our tree
final_results = open('sequence_length.txt', 'w')
final_results.write("The lengths of the recorded sequences as follows: \n" + str(length))

#using seq we can write a fasta file that contains all of our sequences
#will reference this again for the tree
SeqIO.write(seq_records, "homologous_seqs.fasta", "fasta")

##########alignment##########

#okay so clustal wouldnt work on my mac, ebi.ac.uk says that clustal
#has been retired. I couldnt even access it using their online website clustal.org
#to make up for this, the next recommendation on biopython was to use MUSCLE
#so I did the processing using MUSCLE but made it in clustal format

#tell the program where to find muscle
muscle = r"/Users/gavinkoma/Documents/bio-python/week7/submission/muscle3.8.31_i86darwin64"
#set the fasta file to read in and name the aln file to output
#this is the fasta file that we just made moments ago
in_file = "homologous_seqs.fasta"
out_file = "hom_seq.aln"

#i couldnt find the output for my .aln file originally
#im using ATOM editor.
#the .aln file cant be output in atom because of some plugin or sort
#instead had to take my code and run in terminal; terminal then output the
#.aln file in my working directory and from there i was able to continue
muscle_cline = MuscleCommandline(muscle, input=in_file, out=out_file)
#muscle is the location of the executible file, mine is not .exe because i dont
#have a windows computer, mine is darwin64 because i have a mac

#print(muscle_cline)

#this was obtained from stack overflow, my .aln wouldnt print until i included
#this after all of my code; not sure why really but it made it work
get_file = subprocess.Popen(str(muscle_cline),
         stdout = subprocess.PIPE,
         stderr = subprocess.PIPE,
         shell = (sys.platform!="darwin64"))

#this is reading our aln file just to make sure were good to continue
#i have 11 rows with 2592 columns
aln_file = AlignIO.read("hom_seq.aln", "fasta")
print(aln_file)

#align the sequences for the next part
#write the .aln file to a new file that can be processed by phyml
#write aligned sequences to a file to be read by PhyML
#here we take our .aln file and write it to phylip-relaxed format
alignout_fname = "newick_homologous_seqs_phylip_alignment.out"
#this is a parsing operation
AlignIO.write(aln_file,alignout_fname,"phylip-relaxed")



#########PhyML##########
#location of PhyML application
phymlapplicationpath = r"/Users/gavinkoma/Documents/bio-python/week7/submission/PhyML-3.1_macOS-MountainLion"

#doublecheck path
#set up from biopython
assert os.path.isfile(phymlapplicationpath), "PhyML executable missing from path."

#run the program
phymlinstance = PhymlCommandline(cmd=phymlapplicationpath,input=alignout_fname)

#this will call and execute
phymltext,phymltextedit = phymlinstance()



#########ascii##########
#okay so we can use phylo to draw and print the tree to our screen
asciitreefile = alignout_fname + "_phyml_tree.txt"
asciitree = Phylo.read(asciitreefile, "newick")
print("ascii tree:\n")

#draw the tree
Phylo.draw_ascii(asciitree)

#save the tree
with open('asciitree.txt', 'w') as f:
    Phylo.draw_ascii(asciitree, file = f)

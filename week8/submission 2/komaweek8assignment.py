#okay so we need to start by importing all modules as needed
import os
import sys
import itertools
from itertools import permutations

#this will set our working directory to be able to find the necessary documents
currentpath = os.getcwd()
newpath = os.chdir('/Users/gavinkoma/Documents/bio-python/week8')
currentpath2 = os.getcwd()

#i genuinely still dont really understand classes or how to implement them
#so this was written to have functions which can be a part of a class?
#
#it also doesnt really work but i tried to get what i could and write it so something
#might happen but with exams and other projects this week I just couldnt figure it out
#this is a huge preemptive apology for not completing it entirely

#okay so first we start by creating our class.
class Tree(dict):
    def __missing__(self, key):
            value = self[key] = type(self)()
            return value

    def __init__(self, dictionary={}):
        assert type(dict)
        self.self = dict(dictionary)
        for k, dictionary in dictionary.items():
            if isinstance(dictionary, dict):
                self[k] = type(self)(dictionary)
            else:
                self[k] = dictionary

    #so we did the above to make a dictionary
    #basically we need to be able to search through the dictionary
    #this means we need to get keys from the labels and update the dictionary
    #to allow for the searching

    def find_external(nt):
        externalnode = {}
        #search for commas in the newick string
        search = newick.split(',')

        #replace the start parenthesis with nothing
        puncsearch = [c.replace("(", "") for c in search]
        for end in range(len(puncsearch)):
            if ')' in puncsearch[end]:

                #same for end parenthesis
                stringtemporary = puncsearch[emd].split(')')
                stringtemporary2 = stringtemporary[0]
                puncsearch[end] = stringtemporary2

        for i in range(len(puncsearch)):
            v = puncsearch[i].split(':')

            #update value of k
            k = i+1
            externalnode[k] = v, puncsearch[i]

            #return node
        return externalnode

#example function used to find internal nodes
#this makes sense as a function itself but it doesnt really make sense to me how
#to implement it in a class
    def find_internal(nt):

        #start at index 0
        i = 0
        nodeindex = []

        #start within range of the newick string
        #
        for i in range(len(nt)):
            if nt[i] == '(':

                #we know at least 1 open parenthesis at start
                #this was recommendation from dr. hey
                #close parenthesis starts at 0
                openparenthesis = 1
                closeparenthesis = 0

                #update counts as the loop goes through the string
                b = i
                j = i+1

                #this will keep rotating until false
                while True:
                    if nt[j] == '(':
                        #update original value of openparenthesis
                        openparenthesis += 1
                    if nt[j] == ')':
                        #update original value of closeparenthesis
                        closeparenthesis += 1
                        #when these finally equate stop
                    if openparenthesis == closeparenthesis:
                        nodeindex.append(nt[b:j+1])
                        break

                    j += 1

                #give locations of internal node
        return nodeindex


#im so stressed why cant i figure this out


# newick = findinternalnodes("((((D._melanogaster:0.08429511,D._pseudoobscura:0.06972705):0.03556739,S._lebanonensis:0.12220111):0.04925939,D._mulleri:0.08166394):0.03844167,(S._albovittata:0.04424925,D._crassifemur:0.05455754):0.07145753,(D._nigra:0.04328887,(((D._affinidisjuncta:0.02115792,D._heteroneura:0.01656576):0.01142038,D._adiastola:0.03221973):0.00441784,D._mimica:0.02343149):0.01492077):0.04262717)")
# print (newick)

nws = open("drosophilatree.nwk",'r').readline().strip()

#nt = open('test.txt', 'r').readline()

nt = open('drosophilatree.nwk', 'r').readline()
print(nt)
print()


external_nodes = find_external(nt)
internal_nodes = find_internal(nt)

## play with newick format
## build a random newick string

import random

def pick2(picklist):
    """ pick two items in the list
        This picks randomly.  For your program you will pick items
        using the UPGMA algorithm   """
    n = len(picklist)
    if n<2 :
        print ("two few items in list ")
        exit()
    p1 = random.randint(0,n-1)
    p2 = random.randint(0,n-1)
    while p2 == p1 :
        p2 = random.randint(0,n-1)
    return picklist[p1], picklist[p2]

def buildnewnode(node1, node2):
    """ build a newickformat node by combining node1 and node2
        node1 and node2 are strings"""
    return "(" + node1 + "," + node2 + ")"


samplist = []
n = int(input (" enter number of sequences : "))
##n = 10
for i in range(n):
    samplist.append(str(i))

while len(samplist) > 1:
##    print samplist
    (node1,node2) = pick2(samplist)
    samplist.remove(node1)
    samplist.remove(node2)
    samplist.append(buildnewnode(node1,node2))

print (samplist[0] + ';')






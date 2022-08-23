
import os
import sys
import random
import math
import re


class edge:
    """
        an edge on the tree
    """

    def __init__(self,id=-1, up = None, dn = -1, t = 0.0): # dn = down; t = # descendents
        """
            nup is the # descendants (fix at 2)
            up is a list of the descendants
            dn is the down ancestor
            t is the length of the edge  (not the time at the bottom)
            use the position in nodelist as the id #
        """
        self.id = id
        self.nup = 2 # biforcating tree; only 2 descendents
        if up != None:
            self.up = list(up) # up ancestor
        else:
            self.up = []
        self.dn = dn # down ancestory
        self.t = max(0.0,t) # length of edge?

    def update(self,id = None, upedge = None, up = None, dn = None, t = None):
        # if you have an edge and want to change some values
        """
            for updating any of the basic variables belonging to an edge
        """
        if id != None:
            self.id = id
        if upedge != None: ## add the upedge to the list up
            assert upedge not in self.up
            self.up.append(upedge)
            self.nup += 1
        if up != None:
            self.up = up
        if dn != None:
            self.dn = dn
        if t != None:
            self.t = max(0.0,t)

    def isexternal(self):
        """
            True if no daughter edges
        """
        return self.up == []

    def __str__(self):
        """
            create a string with information for using print()
        """
        s =  "id %d nup %d "%(self.id,self.nup)
        if self.up == []:
            s += "[]"
        else:
            s += '['
            for i in range(self.nup):
                if i < self.nup-1:
                    s += "%d,"%self.up[i]
                else:
                    s += "%d"%self.up[i]
            s += ']'
        s += " dn %d"%self.dn
        s += " time %.3f"%self.t
        return s

class tree(dict):
    """
        a tree class, is a subclass (inherits from) the dictionary type,
        contains a phylogenetic tree
        positive integers are used as labels
    """

    def __init__(self, filename):
        """
            initialize the dictionary with a single root edge
        """

        self.tlen = 0.0 # tot len of tree branches
        self.tmrca = 0.0 #time of most recent common ancestor
        label = 0
        self[label] = edge(id = label,up = [],dn = -1,t = 0.0) # add edge; this is the root of the tree
        # label is the key of the dictionary and edge is the value
        self.nextlabel = label + 1 # set ahead of time to be equal to label + 1
        self.rootid = label # root id
        self.numexternal = 1 # number of external edges


    def __add__(self, addtime):
        """
        overload addition +=  add addtime to all extern edges
        """
        for key in self.keys():
            if self[key].isexternal():
                self[key].t += addtime
        self.tlen += self.numexternal * addtime ## increment the length of the tree
        self.tmrca += addtime
        return self


    def growrandom(self,addtime):
        """
            if tree has more than one edge
                add time to all external edge lengths and then

            if only one edge,  this is the root and do not add time
            randomly pick an edge to split into two daughter edges
        """
        def add_daughters ():
            """
                pick an external edge at random and make two daughters
            """
##            print(self)
            while True:
                x = random.choice(list(self.keys()))
                if  self[x].isexternal():
                    break
            self[self.nextlabel] = edge(id = self.nextlabel,up = [], dn = x,t = 0.0) # add new edge to tree; down edge is x, i.e. the label that i picked to be the 2daughters

            tempup = [self.nextlabel]
            self.nextlabel += 1
            self[self.nextlabel] = edge(id = self.nextlabel,up = [], dn = x,t = 0.0)
            tempup.append(self.nextlabel) # appends next label inside tempup
            self.nextlabel += 1 # increment next label
            self[x].update(up = tempup) # do entire thing again with same down edge, x; aka you put both daughters into tree;update x next daughter
            self.numexternal += 1
            return

        if len(self) > 1:
            self += addtime; # overridden + sign and you send addtime up to __add__ overloaded fxn above and then add addtime to all of the external edges
        add_daughters()
        return

    def getedgetotaltime(self,e):
        """
            return the time at the bottom of edge e
            have to sum all the descendant edges
        """
        tempt = self[e].t
        while self[e].up != []:
            e = self[e].up[0]
            tempt += self[e].t
        return tempt

    def newick(self):
        """
            return a newick string for self

        """

        def innernewick(self,tempedge):
            """
                recursive
            """
            if self[tempedge].isexternal():
                return str(tempedge)
            else:
                tempnodeinfolist = []
                for i in range(2):
                    tempupid  = self[tempedge].up[i]
                    tempnodestr = innernewick(self,tempupid) # innern
                    temptime = self[self[tempedge].up[i]].t
                    tempnodeinfolist.append(tempnodestr + ":%.5f"%(temptime))
                tempbuildnode = "(" + tempnodeinfolist[0] + ',' + tempnodeinfolist[1] + ')' + str(tempedge)
                return tempbuildnode
            return

        newickstr = innernewick(self,self.rootid) + ";" # innernewick makes newick string
        return newickstr

    def sumbranchlengths(self):
        """
            return a simple sum of branch lengths

        """
        sumt = 0.0
        for e in self:
            sumt += self[e].t
        return sumt

    def checktree(self):
        """
            does several checks of integrity
            kind of slow
        """
        sumt = 0.0
        countexternal = 0

        for e in self:
            if e != self.rootid:
                if (e == self[self[e].dn].up[0] or e == self[self[e].dn].up[1]) is False: # check that an up edge and its dn ege identify each other
                    print (self[e])
                    raise Exception(" up dn failure in checktree:  edge %d"%(e))
                if self[e].up != [] and self[e].up[0] == self[e].up[1]:  # check that both up edges are different
                    raise Exception (" up failure for edge %d:  up[0] %d up[1] %d"%(e,self[e].up[0],self[e].up[1]))
            else:  # its the root and should not have a dn edge or a time
                if self[e].dn != -1:
                    raise Exception (" rootid: %d  has a down edge"%(self.rootid))
                if self[e].t != 0.0:
                    raise Exception (" rootid: %d  has a t value"%(self.rootid))
        for e in self:   # loop over all edges,  sum length, and check that each edge's path to the root has length = tmrca
            sumt += self[e].t
            if self[e].isexternal():
                countexternal += 1
                d = e
                tmrcacheck = 0.0
                while self[d].dn != -1:
                    tmrcacheck += self[d].t
                    d = self[d].dn
                if math.isclose(tmrcacheck,self.tmrca) is False:
                    raise Exception("tmrca check failed: tmrcacheck %.4f  self.tmrca %.4f"%(tmrcacheck,self.tmrca))
        if math.isclose(sumt,self.tlen) is False:
            raise Exception("tlen check failed: sumt %.4f  self.tlen %.4f"%(sumt,self.tlen))
        if countexternal != self.numexternal:
            raise Exception("external count failed: count %d  self.numexternal %d"%(countexternal,self.numexternal))

    def gettreestats(self):
        """
            print length and edge count summaries
        """
        sumexlen = 0.0
        sumintlen = 0.0
        exc = intc = 0
        for e in self:
            if self[e].isexternal():
                exc += 1
                sumexlen += self[e].t
            else:
                intc += 1
                sumintlen += self[e].t
        try:
            if intc > 0:
                info = "Length : %.3f  TMRCA: %.3f #edges: %d  #internal: %d (mean length: %.4f)  #external: %d (mean length: %.4f)"%(self.tlen,self.tmrca,len(self),intc,sumintlen/intc,exc,sumexlen/exc)
            else:
                assert exc == 1
                info = "Length : %.3f  TMRCA: %.3f #edges: %d  #internal: %d #external: %d (mean length: %.4f)"%(self.tlen,self.tmrca,len(self),intc,exc,sumexlen/exc)
        except Exception:
            info = "problem getting stats"
        return info

    def __str__(self): # overloaded str returns string that includes whatever
        # gettreestats returns and it's also going to add a newick string
        s =  self.gettreestats() + "\n"
        s += self.newick() + "\n"
        return s

##a = edge(id=5,t=3.4)
##random.seed(11) # don't need this line
# maybe can get user to input seed or get seed from clock


t = tree("drosophilatree.nwk")
print(t)
numnew = 10
for i in range(numnew):
    time = 1.0
    t.growrandom(time)
    print(t)





# build a list of all the internal nodes of a newick string, i.e. all substrings with bracketing parentheses
# this does not do anything with the external nodes

nws = open("drosophilatree.nwk",'r').readline().strip()

# remove semicolon
nws = nws[:nws.rfind(';')]

#intialize nodestringlist and nodelabelist
#nodelabellist holds a numerica label for each internal node
nodestringlist = [nws]
nextnodelabel = 0
nodelabellist = [nextnodelabel]

# i indexes the nodes
# this outer loop, loops over the nodestrings
# the inner loop adds new nodestring to the end of the list
i = 0
while True:
    if i >= len(nodelabellist):
        break
    nodestring = nodestringlist[i]
    print(nodestring+"\n")  # just for checking
    # make a new string from the nodestring but without opening and closing parentheses
    nodestring_strip_parens = nodestring[nodestring.find('(')+1:nodestring.rfind(')')]

    # counters and markers for positions in noestring_strip_parens
    p = 0
    numopenparens = 0
    numcloseparens = 0
    pstart = -1
    while True:
        numopenparens += nodestring_strip_parens[p] == '('
        numcloseparens += nodestring_strip_parens[p] == ')'
        if numopenparens == 1  and numcloseparens == 0 and pstart == -1:   # set marker for beginning of a nodestring
            pstart = p
        if numcloseparens == numopenparens and numcloseparens != 0:  # reached the end of a nodestring
            newnodestring = nodestring_strip_parens[pstart:p+1]
            nodestringlist.append(newnodestring)   # add the newlly found nodestring to the end of the list
            nextnodelabel += 1  # set the label for the newly found nodestring
            nodelabellist.append(nextnodelabel) # put the label in the list
            # reset counters and marker so we are ready to handle the next nodestring we find
            numopenparens = 0
            numcloseparens = 0
            pstart = -1
        p += 1
        if p == len(nodestring_strip_parens): # readed the end
            i += 1
            break

print(len(nodestringlist))
print(len(nodelabellist))


nodes = []
for node in nodestringlist:
    nodes.append(edge(node))



tree = {k: v for k, v in zip(nodelabellist, nodes)}












##tree = {k: v for k, v in zip(nodelabellist, nodestringlist)}
##
##
##x = tree(tree, nws)

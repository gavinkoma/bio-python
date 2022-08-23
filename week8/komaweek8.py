import itertools
from itertools import permutations
import os
import sys

currentpath = os.getcwd()
newpath = os.chdir('/Users/gavinkoma/Documents/bio-python/week8')
currentpath2 = os.getcwd()

def newick_parser(newick):
    ''' this function will parse through a newick string and create a
        nested dictionary '''

    # find symbols within newick string
    symbols = re.findall(r"([^:;,()\s]*)(?:\s*:\s*([\d.]+)\s*)?([,);])|(\S)",
                        newick+";")

    def nodes_(nextid = 0, parentid = -1):
        ''' starting with the root node with an ancestor of -1.
            this function goes through each node and nests it within
            its ancestors '''

        thisid = nextid;
        children = []

        name, length, semicolon, paren = symbols.pop(0)
        if paren == "(":
            while paren in "(,":
                node, paren, nextid = nodes_(nextid+1, thisid)
                children.append(node)
            name, length, semicolon, paren = symbols.pop(0)

        return {"id": thisid, "species_name": name,
                "branch_length": float(length) if length else None,
                "parent_id": parentid,
                "children": children if children != [] else None},semicolon, nextid

    return nodes_()[0] # returns just the newick dictionary


# I rooted the drosophilatree.nwk file.
    # So please download the binarydrosophilatree.nwk file that I
    # uploaded to canvas.
nws = open("binarydrosophilatree.nwk",'r').readline().strip()
print('Rooted newick string:', nws, '\n\n\n')

# parse newick string into dictionary
    # keys are ['children', 'length', 'id', 'name', 'parentid']
    # values are from the newick string
nd=newick_parser(nws)
print('Original newick dictionary:', nd, '\n\n\n')

# obtain values from the newick dictionary for nodes and
    # lists for the ancestors of those nodes
ancestors = obtain_vals(nd, 'parent_id')
ids = obtain_vals(nd, 'id')

# create a new (simpler) dictionary with the nodes as the keys
    # and the ancestors as the values
d = defaultdict(list)
for key, value in zip(ids, ancestors):
    d[key].append(value)

# add all ancestors to nodes
for key in d:
    d[key] = [x for x in ancestors if key > ancestors[x]]
for k, v in d.items():
    new_list = []
    for item in v:
        if item not in new_list:
            new_list.append(item)
    d[k] = new_list

# get rid of duplicate ancestors
    # and make sure values of ancestors are < values of nodes
dnew = {k:[vi for vi in v if k != vi] for k,v in d.items()}
newn = {k:[vi for vi in v if k > vi] for k,v in dnew.items()}

# create a list of dictionary with node and ancestors list pairs
temp = []
for key,val in newn.items():
    temp.append({'node':key, 'ancestors':val})

# create an instance of the Tree class to print newick tree
tree = Tree()
for node in temp:
    tree.insert(node['node'], node['ancestors'])

print('Original newick dictionary',tree,'\n-----------\n')


# prune and regraft
count=0
for i in range(10): ## iterate through loop 10x
    count+=1

    print("Iteration:",count) # how many times you've gone through loop

    # print random node and its ancestors to be pruned
    print('The randomly picked node is',key,'with ancestors',val)

    # print regrafted newick
    print('\nUpdated newick dictionary',tree,'\n---------------\n')

    # pick one random node (i.e. key) and its ancestors (i.e. vals)
    for key, vals in random.sample(tree.items(), 1):

        # delete the node and its ancestors
        del tree[key]

        # add the deleted node/ancestors set back into the newick dictionary
        tree[key] = vals

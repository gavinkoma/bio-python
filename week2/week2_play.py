##print("hello world")
##a = open("test.txt","a")
##type (a)
##dir (a)
##a.write("hello file world xxx zzzz")
##a.close()


fname = "Dromel_Adh.fasta"
adhfile = open(fname,"r")
linelist = adhfile.readlines()
adhfile.close()

##a=1
##b = -3
##if (a==2):
##    print (" a equals 2")
##elif (a==1) :
##    print (" a equals 1")
##    if b < 0:
##        print("negative b")
##else:
##    print("a is not 1 or 2")

##a = 0
##while True :
##    print (a)
##    a += 1
##    if a >= 5:
##        break


##a = [1,2, "hello", ["x","y" ],3e-9]
##a = "mystring"
##ai = iter(a)
##anew = list(ai)
##print(a)
##print(anew)

##c=["dog","cat","fish","duck","butterfly"]
##for cpart in c:
##    print (cpart)

##for char in "abcdef":
##    print (char)

##for i in range(0,5):
##    print (i)

##a = "mystring"
##for x in range(0,len(a),2):
##    print(a[x])

##
##for x in a:
##    print(x)


def myfunc():
    # comment example 
    """ show example of using triple
        quote string in a function"""
    return

def myprint (toprint) :
    """simple print function example"""
    print ("now printing: ",toprint)

def plusone (addto) :
    """ simple addition function example"""
    return addto + 1


def addtwo(f,s):
    x = f+s
    return x

def rettwo(x):
    return x*x,  x+x


def playlist(x):
    sum = 0
    for xval in x:
        sum += xval
    return sum

a = [[0.578789,0.709068,0.133332],
    [0.256684,0.217213,0.918261],
    [0.059334,0.349801,0.208787],
    [0.709623,0.751263,0.614539],
    [0.692426,0.688036,0.309793],
    [0.736131,0.861346,0.455957],
    [0.844321,0.120789,0.836109]]


import os


currentpath = os.getcwd()
newpath = os.chdir('/Users/gavinkoma/Documents/bio-python/week8/inclass')
currentpath2 = os.getcwd()



"""
    class dataset example for Biological Models in Python
"""

#we need to make this a subclass of built-in type
class dataset(list):
    """
        an instance of a dataset is mostly a list of floating point values
        added functionality includes __len__(), __str__()  calcmean() and calcvariance()
    """

    def __init__(self,filename):
        """
            filename is the name of the file one value per row to be added to self.vals
        """
        self.vals = []
        self.fname = filename
        with open(filename,'r') as fp:
            for line in fp:
                self.vals.append(float(line))
        fp.close()

    def __str__(self):
        """
            build a string with information about self
        """
        s = "filename:\n\t" + self.fname + '\nValues {}:\n'.format(len(self))
        for v in self.vals:
            s += str(v) + " "
        s += "\n"
        return s

    def calcmean(self):
        sum = 0.0
        for v in self.vals:
            sum += v
        return sum/len(self.vals)

    def calcvariance(self):
        sum = 0.0
        sumsq = 0.0
        for v in self.vals:
            sum += v
            sumsq += v*v
        n = len(self.vals)
        variance = (sumsq - pow(sum,2)/float(n))/float(n-1)
        return variance



d1 = dataset("datafile1.txt")
print(d1)
print (len(d1),d1.calcmean(),d1.calcvariance())

d2 = dataset("datafile2.txt")
print(d2)
print (len(d2),d2.calcmean(),d2.calcvariance())

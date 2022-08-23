import sys
import os
import numpy as np
import pandas as pd

#this will set our working directory to be able to find the necessary documents
currentpath = os.getcwd()
newpath = os.chdir('/Users/gavinkoma/Documents/bio-python/week11')
currentpath2 = os.getcwd()


#start by loading the .tsv file
#and indicate the seperator
filedata = pd.read_csv('ENS_Genic_Codon_Branch_ADJ_Residuals.tsv',sep='\t')

#replace all 0s' with NaN
filedata.replace(0,np.nan,inplace=True)

#next we need to build a new DataFrame
#with one row per gene and one column that contains
#the mean branch lengths

#so lets start by making a mean column

#skipna = True allows us to skip NaNs
filedata['meanbranchlength']=filedata.mean(axis=1,skipna=True)

#so whats cool is that the first column of this data frame is unnamed
#so instead of creating a whole new column and repopulating it we can just rename it
filedata.rename(columns={filedata.columns[0]:'gene'},inplace = True)

filedatanew = pd.DataFrame(filedata,columns=['gene','meanbranchlength'])

print('These are the first rows of the data frame:\n\n' + str(filedatanew.iloc[:10,:]))

#okay so now to finish we just need to print the shape of this DataFrame
#and the mean of all the meanbranchlengths, across genes, to a file

#how do we get the mean of means tho
#uhhhh
#okay so we want to at least select the column meanbranchlength
#and then well want to select all the rows that in that column
#and then average them for the mean
#which would be the row axis??

dataframeshape = filedatanew.shape
print(dataframeshape)

meanofmeans = filedatanew['meanbranchlength'].iloc[:].mean(axis=0)
print(meanofmeans)

file = open('GavinKomaWeek11pt3Assignment.txt','w')
file.write('Shape of Dataframe:\n')
file.write(str(filedatanew.shape))
file.write('\n\nMean of means of measured branch lengths:\n')
file.write(str(meanofmeans))
file.close()

import sys
import os
import pandas as pd

#this will set our working directory to be able to find the necessary documents
currentpath = os.getcwd()
newpath = os.chdir('/Users/gavinkoma/Documents/bio-python/week11')
currentpath2 = os.getcwd()


filedata = pd.read_csv("Waterbody_Classifications.csv")


#okay so we need to use correlation method in pandas
#to calculate but we should be weary of the columns that dont
#have numbers because they should be NaN's

filedata_corr = filedata.select_dtypes(include=['number']).corr(method='pearson')
print(filedata_corr)

print('Shape of Dataframe:\n',filedata.shape)
print('Column names:\n',list(filedata.columns))
print('Data Types:\n',filedata.dtypes.to_string())
print('Pearson Correlation:\n', filedata_corr.to_string())

file = open('GavinKomaWeek11pt2Assignment.txt','w')
file.write('Shape of Dataframe:\n')
file.write(str(filedata.shape))
file.write('\n\nColumn names:\n')
file.write(str(list(filedata.columns)))
file.write('\n\nData Types:\n')
file.write(str(filedata.dtypes.to_string()))
file.write('\n\nPearson Correlation:\n')
file.write(str(filedata_corr.to_string()))
file.close()

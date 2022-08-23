from Bio import SeqIO
import collections
import time
import threading
import multiprocessing
import sys
import os


#this will set our working directory to be able to find the necessary documents
currentpath = os.getcwd()
newpath = os.chdir('/Users/gavinkoma/Documents/bio-python/week10')
currentpath2 = os.getcwd()

'''
Michelle Joyce
Week 10 assignment 
'''
import sys
import os
from Bio import Entrez
from Bio import SeqIO
import threading
import multiprocessing
from multiprocessing import Process
import time



def jobs(task, file_num):

    # show that the job is starting
    if task == 'thread':
        print('Starting', threading.current_thread().getName())
    else:
        print('Starting process', file_num)

    files = ['Myotis_aligned_small.fasta', 'opuntia.fasta', 'porcelaincrab_aligned.fasta', 'pyrus.fasta']
    # read the fasta file
    # make a list of SeqRecords
    sr = []

    data = SeqIO.parse(files[file_num], 'fasta')
    for s in data:
        rec = s.seq  # this gets just the SeqRecord from the file
        sr.append(rec)  # then add it to the list
   
    #print(sr)
    # calc num of records in each list 
    num_rec = len(sr)

    # and total sequence length for each file - sum the lengths of all the records 
    total_len = []
    for i, seq in enumerate(sr):
        each_len = len(sr[i])
        total_len.append(each_len)
    sum_total = sum(total_len)

    # print values to screen 
    print('In file: ' + files[file_num])
    print('There are ' + str(num_rec) + ' records.')
    print('The total sequence length is ' + str(sum_total))

    # show that the job is ending
    if task == 'thread':
        print( 'Ending', threading.current_thread().getName())
    else:
        print('Ending process', file_num)


# main function of the program 

if __name__=="__main__":
    # can be called by passing 4 combinations of arguments, which can be accessed by sys.argv[]
        # thread onebyone
        # thread afterall
        # multiprocess onebyone
        # multiprocess afterall 
   
    # begin timing
    start_time = time.time()

    # print which module is running
    print('Module: ', sys.argv[1]) 
    print('Join Condition: ', sys.argv[2])
    f1 = 'Myotis_aligned_small.fasta'
    f2 = 'opuntia.fasta'
    f3 = 'porcelaincrab_aligned.fasta'
    f4 = 'pyrus.fasta'
    files = [f1, f2, f3, f4]
    numfiles = 4
    
    t = [] # a list of threads
    # this is the treading module
    if sys.argv[1] == 'thread':
        task = 'thread'
        
        for f in range(numfiles):
            t.append(threading.Thread(name='thread_' + str(f) + "_job", target=jobs, args = (task, f)))
            t[f].start()
            if sys.argv[2] == 'onebyone':
                t[f].join()

        if sys.argv[2] == 'afterall':
            for i in range(len(files)):
                t[i].join()

    # this is the multiprocess module
    procs = []
    if sys.argv[1] == 'multiprocess':
        task = 'multiprocess'
        for x in range(numfiles):
            proc = Process(target=jobs, args=(task,x))
            procs.append(proc)
            print("starting",x)
            proc.start()
            if sys.argv[2] == 'onebyone':
                proc.join()

        if sys.argv[2] == 'afterall':
            for proc in procs:
                proc.join()


    stop_time = time.time()  # end timing
    total_time = stop_time - start_time

    print(total_time)

    # write time to a file
    output = open('time_results.txt', 'a')
    line = str(sys.argv[1]) +' '+ str(sys.argv[2]) +' '+ str(total_time)
    output.write(line +'\n')
    output.close()
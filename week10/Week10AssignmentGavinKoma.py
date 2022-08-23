#week10assignment Gavin Koma
#okay so we need to start with all of the modules for this assignment:

import sys
import os
from Bio import SeqIO
import collections
import time
import threading
import multiprocessing
from Bio import Entrez
from multiprocessing import Process

#start by definig the allfiles and parsing them
#weve parsed fasta allfiles plenty in the past so this is
#very similar to my submissions from previous assignments

#so this part here shows when the jobs start and exit as well as runs the job function
def jobs(task, filenumber):
    if task == 'thread':
        print('Starting:', threading.current_thread().getName())

    else:
        print('Starting process:', filenumber)

    allfiles = ['Myotis_aligned_small.fasta','opuntia.fasta','porcelaincrab_aligned.fasta','pyrus.fasta']

    #make an empty list of seqrecords to append to
    seqrec = []

    parsed = SeqIO.parse(allfiles[filenumber],'fasta')

    for seq in parsed:
        rec = seq.seq
        seqrec.append(rec)

    numbers = len(seqrec)

    totallength = []

    #so here we take the total length of each file
    #and sum them
    for val, seq in enumerate(seqrec):
        each_len = len(seqrec[val])
        totallength.append(each_len)
    total = sum(totallength)

    #here we print the file name, the total sequences, and the total residues
    print('File: ' + allfiles[filenumber])
    print('\nThere are ' + str(numbers) + ' species.')
    print('\nThe sequence length is ' + str(total))

    #and now we can end the job, this was in the canvas modules; still
    #a bit confused on how threading works
    if task == 'thread':
        print('Ending', threading.current_thread().getName())
    else:
        print('Ending process', filenumber)

#read on one of the stack overflow forms that its good to give the computer
#a small amount of time in between processes? not sure if this is actually needed
#here because of how small the files are but i guess i just included it to be safe
#cant afford a new laptop :')
    time.sleep(5)


#okay so that covers the jobs of the program and now
#we need to write the main portion of the program

if __name__ == "__main__":
    #okay so this is next part is the main portion of the assignment
    #the previous portion has been done x amount of times in previous fasta
    #related assignments but the next part will be the four different methods
        #thread onebyone
        #thread afterall
        #multiprocess onebyone
        #multiprocess afterall
    #well be able to do any of the above four depending on what
    #input arguments we put into the command line with our code

    #we need to start recording the amount of time that the Process
    #that we have chosen takes
    start_timer = time.time()

    #and now we need to print whatever module is running at the time

    #this basically takes everything in the commandline and stores it as an
    #argument list; the arg at 0 is the file name and the index then after all etc..
    #this will print in the terminal before anything comes out so you can read
    #whatever arguments youve entered
    print('Module: ', sys.argv[1])
    print('Join Condition: ', sys.argv[2])

    #assign our allfiles to variables for later reference
    file_1 = 'Myotis_aligned_small.fasta'
    file_2 = 'opuntia.fasta'
    file_3 = 'porcelaincrab_aligned.fasta'
    file_4 = 'pyrus.fasta'
    allfiles = [file_1,file_2,file_3,file_4]
    numfiles = 4

    #its important to include a list for thr threads for the threading module
    threadlist = []

    #this next part is basically copy and pasted from the threading module on canvas
    #the only thing that is changed is that the time tracker is removed and placed outside
    #of any loops that are in the code because we want the full time tracking
    #not a partial time tracking of an inner loop or repeated process
    if sys.argv[1] == 'thread':
        task = 'thread'

#below is the threading module code that i referenced to write the thread portion
#    starttime = time.time()
#     print("Threading module:",task,"  join_one_by_one:",join_one_by_one)
#     t = [] # a list of threads
#     for i in range(numthreads):
#         t.append(threading.Thread(name='thread_' + str(i) + "_job",
# target=sleep_or_loop_or_IO, args = (task, i),))
#         t[i].start()
#         if join_one_by_one:
#             t[i].join()
#     if join_one_by_one is False:
#         for i in range(numthreads):
#             t[i].join()


        #this first portion is the second argument in the command commandline
        #this will give us the different onebyone or afterall options when running
        #the script
        for file in range(numfiles):
            threadlist.append(threading.Thread(name='thread_' + str(file) + "-job", target = jobs, args=(task,file)))
            threadlist[file].start()
            if sys.argv[2] == 'onebyone':
                threadlist[file].join()

        if sys.argv[2] == 'afterall':
            for val in range(len(allfiles)):
                threadlist[val].join()

#below is the multiprocess module that i referenced to write the multiprocess
#portion of code below
    # numprocs = 5
    # procs = []
    # for index in range(numprocs):
    #     proc = Process(target=sleep_or_loop_or_IO, args=(task,index))
    #     procs.append(proc)
    #     print("starting",index)
    #     proc.start()
    #     if join_one_by_one:
    #         proc.join()
    # if join_one_by_one is False:
    #     for proc in procs:
    #         proc.join()
    # stoptime = time.time()
    # print("duration",stoptime-starttime)

    #this portion of the code is just a reformatted and slightly altered
    #version of the multiprocess module on canvas
    #weve removed the location of the start time and altered bits and pieces
    #but overall its the same

    procs = []
    if sys.argv[1] == 'multiprocess':
        task = 'multiprocess'
        for index in range(numfiles):
            proc = Process(target=jobs,args=(task,index))
            procs.append(proc)
            print("starting",index)
            proc.start()
            if sys.argv[2] == 'onebyone':
                proc.join()

        if sys.argv[2] == 'afterall':
            for proc in procs:
                proc.join()

    stop_timer = time.time()
    total_time = (stop_timer - start_timer)

    print(total_time)


    #okay so to finish we need to write all of this to a file and call it a day
    #need to append to the file because i cant figure out how to not get it to overwrite
    #but now i have the issue of it just continuously appending the data to the file
    #so i can only run the program a few times
    finaltime = open('Week10AssignmentTimeTXT','a')
    write = str(sys.argv[1]) + ' ' + str(sys.argv[2]) + ' '+ str(total_time)
    print(write)
    finaltime.write(write+'\n')
    finaltime.close()

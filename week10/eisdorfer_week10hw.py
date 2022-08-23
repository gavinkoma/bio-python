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



##### Functions #####

def read_fasta_file(file, filetype):
    '''
        this function takes in the file name and filetype, i.e. fasta,
        and returns a list of sequences in each file.

        this function also prints the file name, the total sequences
        in the file, and the total residues of all the sequences in each file.
    '''

    srseqlist = [] # empty list for sequences

    for record in SeqIO.parse(file, filetype): # record = seq record
        srseqlist.append(record.seq)  # append all seqs into the empty list

    list_len = len(srseqlist) # find the total sequences in each file

    seq_len_list = [] # empty list for seq lengths
    for num, seq in enumerate(srseqlist):
        seq_len_list.append(len(srseqlist[num])) # append lengths of each seq

    # prints file name, tot seqs, and tot residues
    print('File:', file)
    print('\nThere are', list_len, 'species.',
          '\nThe sequence length is', sum(seq_len_list), '\n\n')

    return  srseqlist # list of seqs




def calc_from_seq_recs(file, filetype, arg):
    '''
        this function prints when the jobs start and exit as well as runs
        the job function.
    '''
    if arg == 'thread':
        print(threading.current_thread().name, 'starting.\n')
    else:
        print(multiprocessing.current_process().name, 'starting.\n')

    proc = os.getpid()
    time.sleep(2)

    seq_list = read_fasta_file(file, 'fasta') # run job

    if arg == 'thread':
        print(threading.current_thread().name,"exiting.\n")
    else:
        print(multiprocessing.current_process().name, 'exiting.\n')

    return



def main(args):

    '''
        this function is the main function of my program.

        it takes in 2 arguments:

            -module arguments or args[0]: (pick one)
            'thread' = argument to run the threading module
            'multiprocess' = argument to run the multiprocess module

            -join() arguments or args[1]: (pick one)
            'onebyone' = join each one after the previous has ended
            'afterall' = join after all have started



        if you run the multiprocess module, please select to 'execute in an
        external system terminal' to see print statements.

            if you are working with Spyder, press Ctrl + F6 --> select
            'execute in an external system terminal' and 'Command line
            options' --> type in commands separated by a space in the
            box to the right of 'Command line options'.

                Select 1 of 4 arguments to type in:
                    thread onebyone
                    thread afterall
                    multiprocess onebyone
                    multiprocess afterall

    '''

    starttime = time.time() # time at start of jobs

    print('Assignment 10\n\n')

    # print module name
    print('Running', args[0] + 'ing module.')

    # print when to join()
    if args[1] == 'onebyone':
        print('Joining each one after the previous has ended.\n')
    elif args[1] == 'afterall':
        print('Joining after all have started.\n')

    # 4 file names
    file1 = "Myotis_aligned_small.fasta"
    file2 = "opuntia.fasta"
    file3 = "porcelaincrab_aligned.fasta"
    file4 = "pyrus.fasta"


    files = [file1, file2, file3, file4] # compile file names into a list

    t = []

    # thread module
    if args[0] == 'thread':
        import threading
        for i,name in enumerate(files): # i = index, name= file name
            # begin threading.Thread()
            t.append(threading.Thread(name='thread ' + str(i+1) + " job",target=calc_from_seq_recs,
                                      args = (name, 'fasta',args[0],)))
            t[i].start() # starts thread

            if args[1] == 'onebyone':
                t[i].join() # join one by one

        if args[1] == 'afterall':
            for i in range(len(files)):
                t[i].join() # join after all threads have started


    # multiprocess module
    elif args[0] == 'multiprocess':
        import multiprocessing
        # begin multiprocessing.Process()
        for i,name in enumerate(files):
            t.append(multiprocessing.Process(name='process ' + str(i+1) + " job",
                                             target = calc_from_seq_recs, args = (name, 'fasta',args[0],)))
            t[i].start()

            if args[1] == 'onebyone':
                t[i].join()

        if args[1] == 'afterall':
            for i in range(len(files)):
                t[i].join()

    stoptime = time.time() # time when jobs are finished

    # added time to keep the external terminal open long enough to read the outputs
        # this is not included in the time duration of the job completion
    time.sleep(10)

    print('\nDuration of job =', stoptime-starttime, 'seconds.')

    print(args[0], args[1],stoptime-starttime, file = open('eisdorfer_jobs_4conditions_.txt', 'a'))



# begin program
if __name__ == '__main__':
    main(sys.argv[1:])

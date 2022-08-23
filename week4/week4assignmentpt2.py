import random
import string

#so first we need to import the random module
#the random module will give us random letters that will populate the generation strings
#the string module will let us generate strings & is used to assign a value to the`
#letters variable below

#this is the main function which references our defined functions as asked in the powerpoint
#this is also allowing us to define the target phrase and all possible letters that may be used
def weasel():
    #this is the target phrase as specified in the homework, i did the string in all lowercase
    #but it can easily be altered to have lowercase, uppercase, and even symbols & numbers
    #inputper = input("Enter a number between 1-100 to specify % chance of mutation per character:")
    target_phrase = "methinks it is like a weasel"
    letters = string.ascii_lowercase + ' '
    #this is our gen0, its our starting point for the cycle
    basegen = 0
    #current string will be altered as the loop progresses, it references our target phrase
    #and is composed of the letters specified in ascii_lowercase
    current_string = createrandomstring(target_phrase, letters)
    #this loop will print the generation and then be updated basegen as the script progresses
    #it outputs each generation and the phrase as it changes and mutates closer to the desired phrase
    print("Generation:",basegen)
    print(current_string)
    while current_string != target_phrase:
        current_string = seqoffspring(current_string,target_phrase,letters)
        basegen += 1
        print("Generation: ",basegen)
        print(current_string)


#we need to create a random string of letters that will act as our base basegen
#we also passed in the target phrase and it will act as the length required of our generation string
#this was just to avoid creating a second variable for just the length
def createrandomstring(target_phrase,letters):
    #here is an empty string that will be filled by random letters below
    #it is the proper length because we reference targetphrase length as a parameter
    stringseq = ""
    for i in range(len(target_phrase)):
        stringseq += letters[random.randint(0, len(letters)-1)]
    return stringseq

#this is our first loop created, previous to this, we would have a python code that would just run
#an infinite amount of times and not stop, we needed to provide the code with parameters that would
#prevent this ()

def seqoffspring(stringseq, target_phrase, letters):
    stringlist = seqmutations(stringseq,letters)
    bestmatch = stringlist[0]
    bestmatchvariable = stringscore(bestmatch,target_phrase)
    for seq in stringlist:
        bestmatchfact = stringscore(seq,target_phrase)
        #if the bestmatch is more similar to the target phrase than the best matche bestmatchvariable
        #then we reassign the value of best match variable to best match bestmatchfact
        #and let the best match string of the 100copies become the new sequence (seq)
        if bestmatchfact > bestmatchvariable:
            bestmatchvariable = bestmatchfact
            bestmatch = seq
    return bestmatch

#this will be our command that creates 100copies, from here we will continue to mutate the copies
#of these 100copies we need to select & mutate the best of them. def seqoffspring will chose the best of the 100copies
#def stringmutation will mutate the strings for us
def seqmutations(stringseq,letters):
    stringlist = []
    for num in range(100):
        stringlist.append(stringmutation(stringseq,letters))
    return stringlist

#here we will mutate the copies to create new strings that will be considered the offspring
#i was unable to incorporate the %chance of mutation rate, I could not figure out what was needed
#and where it was needed to be in order to specify this and pass it in my functions
#my code depends on a 5% chance mutation rate for each character in this part below
def stringmutation(stringseq, letters):
    #inputper = input("Enter a number between 1-100 to specify % chance of mutation per character:")
    result = ""
    for let in range(len(stringseq)):
        if random.randint(0,100) <= 5:
            result += letters[random.randint(0,len(letters)-1)]
        else:
            result += stringseq[let]
    return result

#we also need to determine which letters are in the right replace
#for every letter in the right place, we assign a score
#the score starts at 0 but increases by 1 correct letters
#this lets the computer know that the more string with the higher score is most similar to
#the target phrase and lets us also know that that phrase should be the parent of the
#next generation and mutations should continue from there
def stringscore(stringseq,target_phrase):
    score = 0
    for i in range(len(target_phrase)):
        #compare the target phrase to the newest stringsequence
        if target_phrase[i] == stringseq[i]:
            #if the letter is right then add to the score and assign a new value to the variable
            score += 1
    return score

#runs the script as defined in def weasel()
weasel()

#question 1: write a program to implement the island model of migration
#but with a random change in allele frequency to the deterministic value
print("part1.1")

import random

#we need to receive data numbers from the user
pfreq = float(input("Enter the P frequency on the mainland :"))
p_theta = float(input("Enter the P_0 frequency on the main island in generation 0:"))
m = float(input("Enter the m factor (with a maximum value of 0.01):"))
s = int(input("Enter a random number seed (positive interger) :"))

#now we need to calculate the proper Pt value
#𝑝_(𝑡+1)=𝑚 𝑷+(1−𝑚) 𝑝_𝑡=𝑚(𝑷−𝑝_𝑡 )+𝑝_𝑡
#∆𝑝=𝑝_(𝑡+1)−𝑝_𝑡=𝑚(𝑷−𝑝_𝑡)
#0=𝑚(𝑷−𝑝_𝑡)

#first make the list we will append to

freq = [p_theta]

#for s to function; we need random function as well
#the below function doesnt work without importing python random library
#check first few lines for imported library

random.seed(s)

#this ensures all of our s's are the same with every input
#not really sure why we need this though if the s's are user input
#makes random numbers reproduceable

initialization = 0

#we cannot have more than 10,000 generations
#while initial is less than or equal to 10000
while initialization <= 10000:
    if freq[initialization]<1 and freq[initialization]>0 :

#while initialization is less than or equal to 10000
#and the allele frequency is less than 1 and greater than 0
#we need the random seed now
#uniform function returns a number between a given range
        randomnum = random.uniform(-0.05,0.05)

#now calc pt with the variables obtained

        pval = (m*(pfreq-freq[initialization]))+freq[initialization] + randomnum

        freq.append(pval)

        #initialization=initialization+1, this is the same as the += function
        initialization+=1

    else:
        print("The allele frequency is: " + str(freq[initialization]) + " and it took " + str(initialization) + " generations")

        break

        #we need the break function to stop the while loop from looping

else:
    print("The run takes longer then 10,000 generations. The current allele frequency is: " + str(p_theta))

#question 1: write a program to implement the island model of migration
print("part1.1")

#we need to receive data numbers from the user
pfreq = float(input("Enter the P frequency on the mainland :"))
p_theta = float(input("Enter the P_0 frequency on the main island in generation 0:"))
m = float(input("Enter the m factor :"))
g = int(input("Enter the number of generations for which to calculate the next allele freq :"))

#now we need to calculate the proper Pt value
#𝑝_(𝑡+1)=𝑚 𝑷+(1−𝑚) 𝑝_𝑡=𝑚(𝑷−𝑝_𝑡 )+𝑝_𝑡
#∆𝑝=𝑝_(𝑡+1)−𝑝_𝑡=𝑚(𝑷−𝑝_𝑡)
#0=𝑚(𝑷−𝑝_𝑡)
#p_t+1 = m(P-p_t)+p_t

#first create list for the pfreq

print("part1.2")

freq = [p_theta]

for num in range(0,g):
    pval = (m*(pfreq-freq[num]))+freq[num]
    freq.append(pval)

#print(freq)

#print p_t as t goes from 0 up to and including g
print("The initial allele frequency is: " + str(p_theta))
for num in range(1,g+1):
    print("In the " + str(num) + " generation, the allele frequency is: " + str(freq[num]))

#idk why its printing all of my allele frequencies at once and not one at a time
#like in accordance to which generation it is
#the brackets mean index of frequency at whatever the index number is

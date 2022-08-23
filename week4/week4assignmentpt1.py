
#start with the poisson distribution
#import numpy first & now get 1000 samples
#poisson(lam,size)
#lam gives the number of events of the distribution
#size gives us the number of samples
#in our case, we need 1000 samples

import numpy as np
poissonsamples = np.random.poisson(5, 1000)

#print(poissonsamples)

p_list = list(poissonsamples)

#print(p_list)

#now create the uniform distribution
#we will still need 1000 samples

import random

norm_val = []
norm_mu = 10
norm_sigma = 5

for num in range(1000):
    normvalues = random.gauss(norm_mu, norm_sigma)
    norm_val.append(normvalues)


#print(norm_val)


#now make the exponential graph
#we need to have lam for this function
#lambda is defined as 1.0 divided by the desired mean

exp_val = []
explam = 0.5

for expnum in range(1000):
    expvalues = random.expovariate(explam)
    exp_val.append(expvalues)

#print(exp_val)

#now we need to calculate the statistical values of these distribution
mean_poisson = (sum(p_list))/1000
mean_norm = (sum(norm_val))/1000
mean_exp = (sum(exp_val))/1000

print(mean_poisson, mean_norm, mean_exp)


#calculate the variance for the poisson distribution
#make the poilist float for calculation
poi_float_list = []
for val in p_list:
    poi_float_list.append(float(val))

poifloat = poi_float_list     # values (must be floats!)
poimean = mean_poisson  # mean
poivar = sum(pow(poix-poimean,2) for poix in poifloat) / (len(poifloat)-1)
#poistd = pow(poivar,-1/2)
print(poivar)

#calculate the variance for the norm distribution
#print(type(normvalues))
normfloat = norm_val
normmean = mean_norm
normvar = sum(pow(normx-normmean,2) for normx in normfloat) / (len(normfloat)-1) #why does this not work?
print(normvar)

#calculate the variance for the exponential distribution
expfloat = exp_val
expmean = mean_exp
expvar = sum(pow(expx-expmean,2) for expx in expfloat) / (len(expfloat)-1)
print(expvar)

#lines to explain answers and give the answers
line1 = 'The distribution values for the poisson distribution are: ' + str(p_list)
line2 = 'The calculated mean and variance for this distribution, respectively, are: ' + str(poimean) + ' and ' + str(poivar)
line3 = 'The calculated mean of the poisson distribution is extremely close to the given parameter in class.'
line4 = 'The given value being 5 and the calculated mean being 5.027. This is expected as the poisson parameter requires lambda'
line5 = 'Lambda in the poisson distribution is defined by the total number of samples divided by the total number of units. This is very similar to the mean calculation.'
line6 = 'Variance, in the poisson distribution, is also very close to 5. This is expected because theory states that the parameter should equal both the mean AND the variance.'
line7 = 'The distribution values for the normal distribution are: ' + str(norm_val)
line8 = 'The calculated mean and variance for this distribution, respectively, are: ' + str(normmean)  + ' and ' + str(normvar)
line9 = 'The parameters for the normal distribution are mu = 10 and sigma = 5. From this, we can expect that the mean is similar to the specified mean.'
line10 = 'We are also able to expect that the variance is close to the square of our sigma because the square of standard deviation is variance. Thus, 5^2 = 25.'
line11 = 'The distribution values for the exponential distribution are :' + str(exp_val)
line12 = 'The calculated mean and variance for the exponential distribution, respectively, are: ' + str(expmean) + ' and ' + str(expvar)
line13 = 'The input parameter of 0.5 into our exponential function is for the lambda value. Lambda in exponential functions is 1/mu. Therefore, our expected mean is 1/0.5 or 2.'
line14 = 'The variance of calculated from our exponential equivalent to 1/lambda^2, this gives us a value of 4 which is approximately equivalent to our calculated variance.'
e = '\n'

#now we will export this to a .csv for class

result = open('final_answer.txt','w')
result.writelines([line1,e,line2,e,line3,e,line4,e,line5,e,line6,e,line7,e,line8,e,line9,e,line10,e,line11,e,line12,e,line13,e,line14])

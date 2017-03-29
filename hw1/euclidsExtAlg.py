#Joshua Steward
#Lowell Batacan

import random
import matplotlib.pyplot as plt

numBits = int(input("Enter Max Number of Bits: "))

def extendGcd(a, b):
    xCo = 1
    z = 0
    yCo = 0
    t = 1
    numSteps = 0
    #when b is == 0 or less, then the remainder is 0 and we will have the gcd
    while b > 0:
        #increment number of steps in this run for the experiment
        numSteps = numSteps + 1
        #calculates quotient of the current two numbers
        quot = a // b
        #setting previous b to a
        a = b
        #calculating the remainder
        b = a % b
        #getting the previous coefficient
        xCo = z
        #calculating new coefficient
        z = xCo - quot * z
        yCo = t
        t = yCo - quot * t
    return numSteps

listOfBits = []
listOfAve = []
average = 0

#this will run the extended algorithim a set number of times and populate
# a list for the current number of bits used to get numbers for the algorithm
# and a list for the current averages of runs it took to terminate the algorithm

for n in range(1, numBits):
    listOfBits.append(n)
    average=0
    for x in range(1, 100):
        num1 = random.getrandbits(n)
        num2 = random.getrandbits(n)
        count = extendGcd(num1, num2)
        average += count
    totalAverage = average / 100
    listOfAve.append(totalAverage)

#plots the two axis
plt.plot(listOfBits, listOfAve)
plt.ylabel('Averages')
plt.xlabel('Number of Bits')
plt.show()

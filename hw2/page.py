#Joshua Steward
#Lowell Batacan
#10/11/2016
#HW2 - Google Page Rank Algorithm

import fractions
import math

def rank(array, len1):
    converged = False
    d = 0.85
    ranks = []
    numPages = len1
    for i in range(numPages):
        #appends the original base 1/N fractions to the ranks list
        f = fractions.Fraction(1, numPages)
        ranks.append(f)
    previousConvergence = 0
    for rank in ranks:
        previousConvergence += rank
    newConvergence = 0
    convergence = 0.15

    for i in range(100):
    #while converged == False:
    #while abs(newConvergence - previousConvergence) > convergence:
        newConvergence = 0
        for page in range(numPages):
            #search for connections in each page
            connectionsToPage = []
            numOfConnectionsFromPage = 0
            #iterate through values in the page to get the number of connections going out from the page
            for value in array[page]:
                if value == 1:
                    numOfConnectionsFromPage += 1

            for currentPage in array:
                if currentPage[page] == 1:
                    connectionsToPage.append(1)
                else:
                    connectionsToPage.append(0)

            rankAdder = 0
            connectionsIterator = 0

            for conn in connectionsToPage:
                #this will be the number of connections going out from the current page that is coming in to page
                if conn == 1:
                    #first, get connections out from the page that is connecting in to currentPage
                    pageInConnOut = 0
                    currPage = array[connectionsIterator]
                    for c in currPage:
                        if c == 1:
                            pageInConnOut += 1

                    rankAdder += (ranks[connectionsIterator]/fractions.Fraction(pageInConnOut, 1))
                connectionsIterator += 1
            ranks[page] = (1 - fractions.Fraction(d).limit_denominator()) + fractions.Fraction(d).limit_denominator() * (fractions.Fraction(rankAdder).limit_denominator())

        previousConvergence = newConvergence
        for rank in ranks:
            newConvergence += rank

        #if all(x==ranks[0] for x in ranks):
        #    converged = True
    for rank in range(numPages):
        ranks[rank] = str(ranks[rank])
    return ranks

#creating array
f = open('data.txt', 'r')
with f as file:
    matrix = [[int(digit) for digit in line.split()] for line in file] #reads file into the 2d array

numrows = len(matrix)    # rows in your example
numcols = len(matrix[0]) # columns in your example
num_of_ele = sum(len(x) for x in matrix)
ranks = rank(matrix, numrows)
print(matrix)
print(ranks)
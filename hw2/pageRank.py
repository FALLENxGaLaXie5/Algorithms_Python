def page_rank(array, len1):
    sum(1 for row in array
        for i in row if i)
    d = 0.8 # damping factor
    ranks = [[]]
    num_of_rows = len1 # number of rows
    num_of_elements = num_of_ele = sum(len(x) for x in array) # number of elements in each row

    for page in array:
        for pages in array[page]:
            ranks[page [pages]] = 1/num_of_elements

    for i in num_of_ele:
        newranks = [[]]
        for page in array:
            newranks = (1-d)/num_of_elements
            for pages in array[page]:
                if page in array[pages]:
                    newranks = newranks + d * (ranks[pages]/len(array[pages]) )
                newranks[page[pages]] = newranks
            ranks = newranks
        return ranks


#creating array
f = open('data.txt', 'r')
with f as file:
    matrix = [[int(digit) for digit in line.split()] for line in file] #reads wahts in the file into the 2d array

numrows = len(matrix)    # rows in your example
numcols = len(matrix[0]) # columns in your example
num_of_ele = sum(len(x) for x in matrix)
print(matrix)



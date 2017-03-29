# Group 10: Jessica Perez, Alinda Heng, and James Allen
# Assignment 3
# 10/17/2016

import sys

'''
Need to do:
Get data from file rather than hardcoded.

'''

# Name of input file.
fileName = './input.txt'

# Reads matrix from file.
with open(fileName) as file:
	# Read string from file.
	gridString = file.readlines()


# Size of grid.
#n = 2
n = 3

# Array of edges. These need to be read in from the input.
#edge = [(1, 2), (3, 4), (2, 4), (1, 3)]
#edge = [(1, 2), (1, 4), (2, 5), (3, 6), (4, 7), (5, 6), (5, 8), (6, 9), (7, 8), (8, 9)]

#print("Edges:", edge)
fileobj = './edges.txt'
def read_by_tokens(fileobj):
    for line in fileobj:
        for token in line.split():
            yield token

with open('./edges.txt') as f:
    tokenized = read_by_tokens(f)

    # read first two tokens separately
    first_token = next(tokenized)
    second_token = next(tokenized)

    for token in tokenized:
        # loops over all tokens *except the first two*
        print(token)


num = len(token)
print("number of edges is ",num)
# Array of corresponding costs and its index.
# The index will be added in a loop.
cost = []

for x in range (0, num):
	temp = 1	# This is where the cost read in from the file will go.
	cost.append((temp, x))

# Hardcoded.
#cost = [(9, 0), (5, 1), (6, 2), (2, 3)]
cost = [(1, 0), (5, 1), (1, 2), (5, 3), (2, 4), (1, 5), (4, 6), (3, 7), (3, 8), (2, 9)]

# Ordered list containing index of edge with the lowest costs and cost of edge.
cost = sorted(cost)
print("Sorted costs from least to greatest:", cost)

# Array that contains the indices of edges in the minimum spanning tree.
mcst_index = []

# Add the smallest value to the mcst_index array.
mcst_index.append(cost[0][1])

#print(mcst_index)

# Current list of connected edges.
connected = []

# Add edge with smallest value.
connected.append(edge[mcst_index[0]][0])
connected.append(edge[mcst_index[0]][1])

#print(connected)

# Traverse through cost array, adding in the indices of smallest costs to mcst_index.
# If the edge creates a cycle, do not add it and skip to the next item in the cost array.

# If both edges are already visited.
for x in range (1, num):
	if edge[cost[x][1]][0] in connected and edge[cost[x][1]][1] in connected:
		# Pass. Do not add this edge.
		pass
	else:
		# Add the index of the cost to mcst_index.
		mcst_index.append(cost[x][1])

		# Last item in mcst_index.
		last = len(mcst_index) - 1

		# Add the edge of
		if edge[cost[x][1]][0] in connected:
			connected.append(edge[mcst_index[last]][1])
		else:
			connected.append(edge[mcst_index[last]][0])

	#print(edge[cost[x][1]][0], edge[cost[x][1]][1])

print("Indices of all connected edges:", mcst_index)
print("All nodes should be connected:", connected)

# Edges in Minimum Cost Spanning Tree
mcst = []
for x in range (0, len(mcst_index)):
	mcst.append(edge[mcst_index[x]])

print("Edges of Minimum Cost Spanning Tree:", mcst)

print()

horNode = 1
vertNode = 1

for x in range (0, n * 2 - 1):
	for y in range (0, n):
		# If y is even, it is a node row. Else it is a blank/edge row.
		if (x % 2 == 0):
			sys.stdout.write("*")
		else:
			currentEdge = (vertNode, vertNode + n)

			# If edge here, then line, else blank.
			if currentEdge in mcst:
				sys.stdout.write("|")
			else:
				sys.stdout.write(" ")

			if (y != n - 1):
				sys.stdout.write("  ")
			#print()
			vertNode = vertNode + 1

		if (x % 2 == 0) and y != n - 1:
			currentEdge = (horNode, horNode + 1)

			# If node is not at the rightmost end of the graph.
			if horNode % n != 0:
				if currentEdge in mcst:
					sys.stdout.write("--")
				else:
					sys.stdout.write("  ")

		if (x % 2 == 0):
			horNode = horNode + 1

	print()




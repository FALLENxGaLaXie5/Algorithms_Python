#Joshua Steward
#Lowell Batacan
# HW4
#Savitch's Algorithm
# 11/07/2016

#global stack variable
stackSav = []

def inputMatrix(r, c):
    n = r * c
    M = [[0 for x in range(n)] for y in range(n)]
    for row in range(r):
        for column in range(c):
            i = row * c + column
            # Two inner diagonals are built in
            #this is used for searching in the adjacency matrix
            if column > 0:
                M[i-1][i] = M[i][i-1] = 1
            # Two outer diagonals are built in as well
            #algorithm will find these paths
            if row > 0:
                M[i-c][i] = M[i][i-c] = 1
    return M


#Called recursively - splits the graph up into smaller bits using divide and conquer
# Returns True if a complete path from one point to the other is found. adds to stack if not
#base case of connected from beginning point to end, or only one connection
# Returns False if a path is not found.
def savitch(G,u,v,k):
    global stackSav
    #global stack is appended with the current boolean predicate
    stackSav.append(("R(" + str(u + 1) + ", " + str(v + 1) + ", " + str(k) + ")"))


    if k == 0:
        #base case #1 - if k is 0, and u is v, that means we have reached the end of the path
        #successfully
        if u == v:
            stackSav.pop()
            return True
        #base case #2 - last edge reached successfully
        elif G[u][v] == 1:
            stackSav.pop()
            return True
    else:
        #calls recursively on every midpoint w in the path
        for w in range(0,pow(2, n) - 1):
            if ((savitch(G, u, w, k - 1)) and (savitch(G, w, v, k - 1))):
                for x in range(len(stackSav)):
                    print(stackSav[len(stackSav) - 1 - x])
                print("<------------------------------------------->")
                stackSav.pop()
                print("True")
                return True

    stackSav.pop()
    return False


print("We want an n x n matrix. \nPlease enter an n:")
n = int(input())

M = inputMatrix(n, n)

#algorithm will search from the top left to the bottom right
savitch(M,0,(n*n)-1,n)
print(stackSav)
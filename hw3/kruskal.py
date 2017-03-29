#Joshua Steward
#Lowell Batacan
#10/24/2016
#HW3 - Kruskal's Algorithm

class Edge:
    def __init__(self, node1, node2, cost, marked):
        self.node1 = node1
        self.node2 = node2
        self.cost = cost
    def __lt__(self, other):
        return self.cost < other.cost
    def displayEdge(self):
        print("Node ", self.node1, " - Node ", self.node2, " costs ", self.cost)
def checkIfEdgeCreatesCycle(edge, originalEdge, kruskalEdges):
    if len(kruskalEdges) > 0:
        currEdge = edge
        for i in kruskalEdges:
            if currEdge.node1 == i.node1 or currEdge.node1 == i.node2 or currEdge.node2 == i.node1 or currEdge.node2 == i.node2:
                currEdge = i
                if currEdge.node1 == edge.node1 and currEdge.node2 == edge.node2:
                    return True
    return False

def createMCST(edges):
    kruskalEdges = []
    for currentEdge in edges:
        #yesNo = checkIfEdgeCreatesCycle(currentEdge, kruskalEdges)
        if checkIfEdgeCreatesCycle(currentEdge, currentEdge, kruskalEdges) is False:
            kruskalEdges.append(currentEdge)
    return kruskalEdges

f = open('data.txt', 'r')
characters = []
edges = []
kruskalEdges = []
with f as file:
    characters = file.readline()
print(characters)
numNodes = int(characters[0])
print(numNodes)

node1 = 0
node2 = 0
cost1 = 0
newEdge = False
nodeOne = False
nodeTwo = False
cost = False
matrix = []
for currentChar in characters:
    if currentChar == '(':
        newEdge = True
        nodeOne = True
        continue
    elif currentChar == ',' or currentChar == ';':
        continue
    if newEdge is True and nodeOne is True:
        node1 = int(currentChar)
        nodeOne = False
        nodeTwo = True
    elif newEdge is True and nodeTwo is True:
        node2 = int(currentChar)
        nodeTwo = False
        cost = True
    elif newEdge is True and cost is True:
        cost1 = int(currentChar)
        cost = False
        newEdge = False
        edges.append(Edge(node1, node2, cost1, False))
nodeNum = 0

edges.sort()
for i in range(numNodes):
    matrix.append([])
    for j in range(numNodes):
        nodeNum += 1
        matrix[i].append(nodeNum)


kruskal = createMCST(edges)


for i in range(numNodes):
    for j in range(numNodes):
        print(matrix[i][j], end="  ")
    print('\n')

print("Minimum cost spanning tree for this graph: ")

for i in kruskal[:-1]:
    i.displayEdge()
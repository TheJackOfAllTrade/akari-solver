import random
import set_priority
import graph

def setProbability(nodeList, node):
    currentNode = nodeList[node]
    probSum = 0
    for x in range(len(currentNode.nodeConnections)): #Adds up all current (Phero * Distance) for every branching node
        probSum += currentNode.nodePheromones[x] * currentNode.nodeDistance[x]

    for x in range(len(currentNode.nodeConnections)): #Same loop as before but actually calculates the probability for each branching node
        currentNode.nodeWeights[x] = (currentNode.nodePheromones[x] * currentNode.nodeDistance[x]) / probSum

    for x in currentNode.nodeConnections: #Recursively calls the same function until every node is visited
        setProbability(nodeList, x)

def startACO(puzzleBoard, nodeList, startNode):
    currentNode = nodeList[startNode]
    nodeChoice = random.choices(currentNode.nodeConnections, weights=currentNode.nodeWeights, k=1) #Gets a random node from the connections of the current node based on the weightings set beforehand
    nodeChoice = nodeList[nodeChoice[0]]
    print("(" + str(nodeChoice.xCoord) + "," + str(nodeChoice.yCoord) + ")")

    puzzleBoard = puzzleBoard[nodeChoice.yCoord][nodeChoice.xCoord].placeBulb(puzzleBoard, nodeChoice.xCoord, nodeChoice.yCoord)
    puzzleBoard = set_priority.setPriorities(puzzleBoard)
    currentNodeList = graph.createGraph(puzzleBoard)
    setProbability(currentNodeList, 0)

    print(currentNodeList)
    if len(currentNodeList) == 1:
        print("ACO Finished")
        return puzzleBoard
    else:
        startACO(puzzleBoard, currentNodeList, 0)

    return puzzleBoard

    
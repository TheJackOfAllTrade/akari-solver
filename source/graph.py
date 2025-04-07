import numpy as np

class Node:
    def __init__(self, nodeID, xCoord, yCoord, nodeConnections, nodeWeights, nodeDistance, nodePheromones):
        self.nodeID = nodeID #So each node can be identified
        self.xCoord = xCoord #Stores the coordinates of the cell that is listed as a possible move
        self.yCoord = yCoord 
        self.nodeConnections = nodeConnections #Lists all connections to that node
        self.nodeWeights = nodeWeights #Follows same order as the connections to list their weightings
        self.nodeDistance = nodeDistance #Follows same order as the connections to list their Distance (Should be all 1 if priotity is not implemented)
        self.nodePheromones = nodePheromones #Follows same order as the connections to list their Pheromones (Updated on pheromone update)

    def updateGraph(startPoint):
        print("Temp String")


def createGraph(puzzleBoard):
    globalNodeList = []
    startNode = Node(0, -1, -1, [], [], [], [])
    globalNodeList.append(startNode)
    global currentID
    currentID = 1
    for y in range(len(puzzleBoard)):
        for x in range(len(puzzleBoard[0])):
            if puzzleBoard[y][x].priority > 0:
                newNode = Node(currentID, x, y, [], [], [], [])
                startNode.nodeConnections.append(currentID)
                startNode.nodeWeights.append(0)
                startNode.nodeDistance.append(1)
                startNode.nodePheromones.append(1)
                globalNodeList.append(newNode)
                currentID += 1
            else:
                continue
    
    return globalNodeList

    print("Woah there bucko, this ain't finished yet")




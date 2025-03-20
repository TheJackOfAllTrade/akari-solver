import numpy as np

class Node:
    def __init__(self, nodeID, xCoord, yCoord, nodeConnections, nodeWeights):
        self.nodeID = nodeID #So each node can be identified
        self.xCoord = xCoord #Stores the coordinates of the cell that is listed as a possible move
        self.yCoord = yCoord 
        self.nodeConnections = nodeConnections #Lists all connections to that node
        self.nodeWeights = nodeWeights #Follows same order as the connections to list their weightings

    def updateGraph(startPoint):
        print("Temp String")

globalNodeList = []

def createGraph(puzzleBoard):

    startNode = Node(0, -1, -1, [], [])
    globalNodeList.append(startNode)
    global currentID
    currentID = 1
    for y in range(len(puzzleBoard)):
        for x in range(len(puzzleBoard[0])):
            if puzzleBoard[y][x].priority > 0:
                newNode = Node(currentID, x, y, [], [])
                startNode.nodeConnections.append(currentID)
                startNode.nodeWeights.append(0)
                globalNodeList.append(newNode)
                currentID += 1
            else:
                continue
    
    return globalNodeList, startNode.nodeConnections

    print("Woah there bucko, this ain't finished yet")




import numpy as np


globalNodePheromones = []

class Node:
    def __init__(self, nodeID, xCoord, yCoord, nodeConnections, nodeWeights, nodeDistance, nodePheromones):
        self.nodeID = nodeID #So each node can be identified
        self.xCoord = xCoord #Stores the coordinates of the cell that is listed as a possible move
        self.yCoord = yCoord 
        self.nodeConnections = nodeConnections #Lists all connections to that node
        self.nodeWeights = nodeWeights #Follows same order as the connections to list their weightings
        self.nodeDistance = nodeDistance #Follows same order as the connections to list their Distance (Should be all 1 if priotity is not implemented)
        self.nodePheromones = globalNodePheromones #Follows same order as the connections to list their Pheromones (Updated on pheromone update)

    def updateGraph(self, puzzleBoard, currentPath, globalNodeList):
        #nodesAdded = 0
        if not self.nodeConnections:
            global currentID
            currentID = len(globalNodeList)
            unused = checkNodeGraph(self, globalNodeList)
            #from main import outputBoard
            #print("----------------------------------------------------------")
            #outputBoard(puzzleBoard, "priority")

            for y in range(len(puzzleBoard)):
                for x in range(len(puzzleBoard[0])):
                    if puzzleBoard[y][x].priority > 0:
                        #nodesAdded += 1
                        newNode = Node(currentID, x, y, [], [], [], [])
                        self.nodeConnections.append(currentID)
                        self.nodeWeights.append(0)
                        self.nodeDistance.append(1)
                        self.nodePheromones.append(1)
                        globalNodePheromones.append(1)
                        globalNodeList.append(newNode)
                        #print("Adding Node: ", newNode.nodeID, " at (", x, ",", y, ")")
                        currentID += 1
                    else:
                        continue
            #print("New Nodes Added: ", nodesAdded)
            #print("----------------------------------------------------------")
            return globalNodeList
        else:
            return globalNodeList

def createGraph(puzzleBoard, globalNodeList):
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
                startNode.nodeDistance.append(puzzleBoard[y][x].priority)
                startNode.nodePheromones.append(1)
                globalNodePheromones.append(1)
                globalNodeList.append(newNode)
                currentID += 1
            else:
                continue
    #print(len(globalNodeList))
    return globalNodeList

def checkNodeGraph(currNode, NodeList):
    return 0

    print("Woah there bucko, this ain't finished yet")




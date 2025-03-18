import numpy as np

class Node:
    def __init__(self, NodeID, XCoord, YCoord):
        self.NodeID = NodeID
        self.XCoord = XCoord
        self.YCoord = YCoord



def createGraph(puzzleBoard):
    adjacencyMat = np.zeros([1,1])
    searchPriority(puzzleBoard, adjacencyMat)
    return adjacencyMat

def searchPriority(puzzleBoard, mat):
    s
    nodeID = 1
    for y in range(len(puzzleBoard)):
        for x in range(len(puzzleBoard[0])):
            if puzzleBoard[y][x].priority != 0:
                newNode = 
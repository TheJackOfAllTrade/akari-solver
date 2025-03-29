import random


def chooseMove(puzzleBoard, nodeList, startNode):
    for i in nodeList[startNode].nodeConnections:
        print(i)
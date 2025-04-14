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

    print("Checking Solution...")
    print("Solved Status: " + str(checkSolution(puzzleBoard)))

    return puzzleBoard

def checkSolution(puzzleBoard):
    for y in range(len(puzzleBoard)):
        for x in range(len(puzzleBoard[0])):
            currCell = puzzleBoard[y][x]
            if currCell.cellType == "-" and currCell.lit == 1:
                print("A - at: (" + str(x) + "," + str(y) + ") is satisfied.")
                continue
            elif currCell.cellType == "0" and checkSatisfied(puzzleBoard, x, y, 0):
                print("A 0 at: (" + str(x) + "," + str(y) + ") is satisfied.")
                continue
            elif currCell.cellType == "1" and checkSatisfied(puzzleBoard, x, y, 1):
                print("A 1 at: (" + str(x) + "," + str(y) + ") is satisfied.")
                continue
            elif currCell.cellType == "2" and checkSatisfied(puzzleBoard, x, y, 2):
                print("A 2 at: (" + str(x) + "," + str(y) + ") is satisfied.")
                continue
            elif currCell.cellType == "3" and checkSatisfied(puzzleBoard, x, y, 3):
                print("A 3 at: (" + str(x) + "," + str(y) + ") is satisfied.")
                continue
            elif currCell.cellType == "4" and checkSatisfied(puzzleBoard, x, y, 4):
                print("A 4 at: (" + str(x) + "," + str(y) + ") is satisfied.")
            elif currCell.cellType == "L" or currCell.cellType == "#":
                print("A " + currCell.cellType + " at: (" + str(x) + "," + str(y) + ") is satisfied.")
                continue
            else:
                print("This solution is not solved")
                return False
    return True


def checkSatisfied(puzzleBoard, x, y, type):
    directions = ["up", "down", "left", "right"]
    count = 0

    if type == 0:
        for i in directions:
            try:
                if i == "up":
                    cell = puzzleBoard[y-1][x]
                    if (y-1 >= 0) and cell.cellType != "L":
                        count += 1
                    else:
                        continue
                elif i == "down":
                    cell = puzzleBoard[y+1][x]
                    if (y+1 <= len(puzzleBoard)) and cell.cellType != "L":
                        count += 1
                    else:
                        continue
                elif i == "left":
                    cell = puzzleBoard[y][x-1]
                    if (x-1 >= 0) and cell.cellType != "L":
                        count += 1
                    else:
                        continue
                elif i == "right":
                    cell = puzzleBoard[y][x+1]
                    if (x+1 <= len(puzzleBoard[0])) and cell.cellType != "L":
                        count += 1
                    else:
                        continue
            except IndexError:
                    continue
    else:
        for i in directions:
            try:
                if i == "up":
                    cell = puzzleBoard[y-1][x]
                    if (y-1 >= 0) and cell.cellType == "L":
                        count += 1
                    else:
                        continue
                elif i == "down":
                    cell = puzzleBoard[y+1][x]
                    if (y+1 <= len(puzzleBoard)) and cell.cellType == "L":
                        count += 1
                    else:
                        continue
                elif i == "left":
                    cell = puzzleBoard[y][x-1]
                    if (x-1 >= 0) and cell.cellType == "L":
                        count += 1
                    else:
                        continue
                elif i == "right":
                    cell = puzzleBoard[y][x+1]
                    if (x+1 <= len(puzzleBoard[0])) and cell.cellType == "L":
                        count += 1
                    else:
                        continue
            except IndexError:
                    continue
            
    if count == type:
        return True
    else:
        return False
    
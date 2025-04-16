import random
import set_priority
import graph

currentPath = []
recursionLimit = 990
currentRecursion = 0

def setProbability(nodeList, node):
    #print(len(nodeList))
    #print(node)
    currentNode = nodeList[node]
    probSum = 0
    for x in range(len(currentNode.nodeConnections)): #Adds up all current (Phero * Distance) for every branching node
        probSum += currentNode.nodePheromones[x] * currentNode.nodeDistance[x]

    for x in range(len(currentNode.nodeConnections)): #Same loop as before but actually calculates the probability for each branching node
        currentNode.nodeWeights[x] = (currentNode.nodePheromones[x] * currentNode.nodeDistance[x]) / probSum

    for x in currentNode.nodeConnections: #Recursively calls the same function until every node is visited
        setProbability(nodeList, x)

def startACO(initialBoard, puzzleBoard, nodeList, startNode):
    global currentRecursion
    global recursionLimit
    global currentPath

    if currentRecursion == recursionLimit:
        print("RECURSION LIMIT REACHED")
        
    else:
        currentRecursion += 1
        currentNode = nodeList[startNode]
        nodeChoice = random.choices(currentNode.nodeConnections, weights=currentNode.nodeWeights, k=1) #Gets a random node from the connections of the current node based on the weightings set beforehand
        nodeChoice = nodeList[nodeChoice[0]]
        print("(" + str(nodeChoice.xCoord) + "," + str(nodeChoice.yCoord) + ")")
        currentPath.append(nodeChoice.nodeID)

        puzzleBoard = puzzleBoard[nodeChoice.yCoord][nodeChoice.xCoord].placeBulb(puzzleBoard, nodeChoice.xCoord, nodeChoice.yCoord)
        puzzleBoard = set_priority.setPriorities(puzzleBoard)
        nodeChoice.updateGraph(puzzleBoard)
        #currentNodeList = graph.createGraph(puzzleBoard)
        setProbability(nodeList, nodeChoice.nodeID)

        #print(currentNodeList)
        if not nodeList[nodeChoice.nodeID].nodeConnections:
            print("ACO Finished")
            print("Checking Solution...")
            solved, fitness = checkSolution(puzzleBoard)
            print("Solved Status: " + str(solved))

            # print("++++++++Current Solution++++++++")
            # print("Current Node Path: ", currentPath)
            # for y in range(len(puzzleBoard)):
            #     line = []
            #     for x in range(len(puzzleBoard[0])):
            #         line.append(puzzleBoard[y][x].cellType)
            #     print(line)
            # print("++++++++++++++++++++++++++++++++")
            # print("++++++++Initial Board+++++++++++")
            # for y in range(len(initialBoard)):
            #     line = []
            #     for x in range(len(initialBoard[0])):
            #         line.append(initialBoard[y][x].cellType)
            #     print(line)
            # print("++++++++++++++++++++++++++++++++")

            if not solved:
                updatePheromones(currentPath, nodeList, fitness)
                currentPath = []
                puzzleBoard = reinitialisePuzzleBoard(puzzleBoard, initialBoard)
                print("RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET ")
                puzzleBoard, currentPath = startACO(initialBoard, puzzleBoard, nodeList, 0)
            else:
                #TODO: Put return here when it's a possible path
                print("Uhhh, I think we're done?")
        else:
            puzzleBoard, currentPath = startACO(initialBoard, puzzleBoard, nodeList, 0)

    return puzzleBoard, currentPath 

def checkSolution(puzzleBoard):
    fitness = 0
    for y in range(len(puzzleBoard)):
        for x in range(len(puzzleBoard[0])):
            currCell = puzzleBoard[y][x]
            if currCell.cellType == "-" and currCell.lit == 1:
                #print("- at: (" + str(x) + "," + str(y) + ") is satisfied.")
                fitness += 1
                continue
            elif currCell.cellType == "0" and checkSatisfied(puzzleBoard, x, y, 0):
                #print("0 at: (" + str(x) + "," + str(y) + ") is satisfied.")
                fitness += 1
                continue
            elif currCell.cellType == "1" and checkSatisfied(puzzleBoard, x, y, 1):
                #print("1 at: (" + str(x) + "," + str(y) + ") is satisfied.")
                fitness += 2
                continue
            elif currCell.cellType == "2" and checkSatisfied(puzzleBoard, x, y, 2):
                #print("2 at: (" + str(x) + "," + str(y) + ") is satisfied.")
                fitness += 2
                continue
            elif currCell.cellType == "3" and checkSatisfied(puzzleBoard, x, y, 3):
                #print("3 at: (" + str(x) + "," + str(y) + ") is satisfied.")
                fitness += 2
                continue
            elif currCell.cellType == "4" and checkSatisfied(puzzleBoard, x, y, 4):
                #print("4 at: (" + str(x) + "," + str(y) + ") is satisfied.")
                fitness += 2
                continue
            elif currCell.cellType == "L":
                #print("L at: (" + str(x) + "," + str(y) + ") is satisfied.")
                fitness += 1
                continue
            elif currCell.cellType == "#":
                #print("# at: (" + str(x) + "," + str(y) + ") is satisfied.")
                continue
            else:
                #print("This solution is not solved")
                return False, fitness
    return True, fitness


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
    

def updatePheromones(nodePath, nodeList, fitness):
    #print("THIS IS WHAT YOU'RE LOOKING FOR")
    nodeIDs = []
    for i in nodeList:
        nodeIDs.append(i.nodeID)
    #print(nodeIDs)
    #print("THIS IS AFTER WHAT YOU'RE LOOKING FOR")
    #print(nodePath)

    startNode = nodeList[0]
    #print("Current Node Pheromone: " + str(startNode.nodePheromones[nodePath[0]]))
    startNode.nodePheromones[nodePath[0]] = pheromoneUpdateEquation(startNode.nodePheromones[nodePath[0]], fitness)
    #print("Fitness: " + str(fitness))
    #print("New Node Pheromones: " + str(startNode.nodePheromones[nodePath[0]]))

    for i in range(len(nodePath) - 1):
        #print(nodePath[i])
        
        currentNode = nodeList[nodePath[i]]
        targetNode = nodePath[i + 1]

        #print("Node Path: ", nodePath)
        #print("currentPheromones: ", currentNode.nodePheromones)
        #print(currentNode.nodeID)
        #print(targetNode)
        currentNode.nodePheromones[targetNode] = pheromoneUpdateEquation(currentNode.nodePheromones[targetNode], fitness)
        #if currentNode.nodeID == 1:
            #print("Node ", currentNode.nodeID, "updated to: ", currentNode.nodePheromones[targetNode])


def pheromoneUpdateEquation(currentPheromone, fitness):
    evapCoef = 0
    return ((1 - evapCoef) * currentPheromone) + fitness

def reinitialisePuzzleBoard(puzzleBoard, initialPuzzleBoard):
    from main import Cell
    puzzleBoard = []
    for y in range(len(initialPuzzleBoard)):
        currentLine = []
        for x in range(len(initialPuzzleBoard[0])):
            currCell = initialPuzzleBoard[y][x]
            initialCell = Cell(currCell.cellType, currCell.lit, currCell.lightable, currCell.priority)
            currentLine.append(initialCell)
        puzzleBoard.append(currentLine)

    return puzzleBoard
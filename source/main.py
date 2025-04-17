import preprocessing as pp
import set_priority as sp
import graph as gr
import ACO


class Cell: #Each cell in the puzzle board and its attributes
    def __init__(self, cellType, lit, lightable, priority):
        self.cellType = cellType
        self.lit = lit #This is whether a cell is lit by a lightbulb or not
        self.lightable = lightable #Don't be fooled, "Lightable" in this case means a cell can't have a lightbulb. I'm just dumb and too lazy to change it
        self.priority = priority

    def placeBulb(self, board, x, y):
        directions = ["up","down","left","right"]
        for l in directions: #I actually can't figure out the logic of why this works as I used it for a complete different reason. If it is removed it will no longer work properly.
            if board[y][x].lightable == True:
                board[y][x].cellType = "L"
                
                for i in directions:
                    stopped = False
                    yCoord = y
                    xCoord = x
                    while not stopped:
                        if board[yCoord][xCoord].cellType == "-" or board[yCoord][xCoord].cellType == "L": 
                            if i == "up":
                                board[yCoord][xCoord].lit = 1
                                board[yCoord][xCoord].lightable = 0
                                if yCoord <= 0:
                                    stopped = True
                                else:
                                    yCoord -= 1
                            elif i == "down":
                                #print(str(yCoord))
                                board[yCoord][xCoord].lit = 1
                                board[yCoord][xCoord].lightable = 0
                                if yCoord >= (len(board) - 1):
                                    stopped = True
                                else:
                                    yCoord += 1
                            elif i == "left":
                                board[yCoord][xCoord].lit = 1
                                board[yCoord][xCoord].lightable = 0
                                if xCoord <= 0:
                                    stopped = True
                                else:
                                    xCoord -= 1
                            elif i == "right":
                                board[yCoord][xCoord].lit = 1
                                board[yCoord][xCoord].lightable = 0
                                if xCoord >= (len(board[0]) - 1):
                                    stopped = True
                                else:    
                                    xCoord += 1
                            else:
                                print("OOOOOOO SCHOOOBIDY LOOBIDY!!")
                        else:
                            #print("Met Cell type [" + board[yCoord][xCoord].cellType + "]. Moving on...")
                            stopped = True
            else:
                print("A lightbulb actually wasn't placed")
                print("-*-*-*-*-*-*-*-*-*CELL*-*-*-*-*-*-*-*-*-*-")
                outputBoard(board, "cell")
                print("-*-*-*-*-*-*PRIORITY*-*-*-*-*-*-*-*-*-")
                outputBoard(board, "priority")
                print("-*-*-*-*-*-*-*LIT*-*-*-*-*-*-*-")
                outputBoard(board, "lit")
        
            
            return board

def readFile(filename): #Reads the file and formats each cell into the Cell object, adding them to the puzzleBoard array
    file = open(filename, "r")
    content = file.readlines()

    for i in content[7:(len(content)-1)]:
        currentLine = []
        for x in i:
            if x == " " or repr(x) == repr("\n"):
                next
            elif x == "-":
                newCell = Cell(x, 0, 1, 0)
                currentLine.append(newCell)
            else:
                newCell = Cell(x, 0, 0, 0)
                currentLine.append(newCell)
        puzzleBoard.append(currentLine)
    file.close()

def outputBoard(puzzleBoard, type):

    # Output Types: (cell, lit, lightable)
    if type == "cell":
        for y in range(len(puzzleBoard)):
            line = []
            for x in range(len(puzzleBoard[0])):
                line.append(puzzleBoard[y][x].cellType)
            print(line)
    elif type == "lit":
        for y in range(len(puzzleBoard)):
            line = []
            for x in range(len(puzzleBoard[y])):
                line.append(puzzleBoard[y][x].lit)
            print(line)
    elif type == "lightable":
        for y in range(len(puzzleBoard)):
            line = []
            for x in range(len(puzzleBoard[y])):
                line.append(puzzleBoard[y][x].lightable)
            print(line)
    elif type == "priority":
        for y in range(len(puzzleBoard)):
            line = []
            for x in range(len(puzzleBoard[y])):
                line.append(puzzleBoard[y][x].priority)
            print(line)
    else:
        print("Not a valid output type")

def writeBoardStateToCSV(puzzleBoard, type):
    # Output Types: (cell, lit, lightable)
    name = filename[8:len(filename)+1] + type + ".csv" 
    filepath = "csv/" + name
    print(filepath)
    csv = open(filepath, "w")
    if type == "cell":
        for y in range(len(puzzleBoard)):
            for x in range(len(puzzleBoard[0])):
                csv.write(puzzleBoard[y][x].cellType + ",")
            csv.write("\n")
    elif type == "lit":
        for y in range(len(puzzleBoard)):
            for x in range(len(puzzleBoard[0])):
                csv.write(str(puzzleBoard[y][x].lit) + ",")
            csv.write("\n")
    elif type == "lightable":
        for y in range(len(puzzleBoard)):
            for x in range(len(puzzleBoard[0])):
                csv.write(str(puzzleBoard[y][x].lightable) + ",")
            csv.write("\n")
    elif type == "priority":
        for y in range(len(puzzleBoard)):
            for x in range(len(puzzleBoard[0])):
                csv.write(str(puzzleBoard[y][x].priority) + ",")
            csv.write("\n")
    else:
        print("Not a valid output type (csv method)")

def createInitialCopy(puzzleBoard):
    initialPuzzleBoard = []
    for y in range(len(puzzleBoard)):
        currentLine = []
        for x in range(len(puzzleBoard[0])):
            currCell = puzzleBoard[y][x]
            initialCell = Cell(currCell.cellType, currCell.lit, currCell.lightable, currCell.priority)
            currentLine.append(initialCell)
        initialPuzzleBoard.append(currentLine)

    return initialPuzzleBoard



######Main#####

print("\n############INITIALISING PUZZLE############")
puzzleBoard = [] #The initial puzzleboard, a 2D array of "Cell" Objects
filename = "puzzles/7x7-1"
readFile(filename) #Initialises puzzleBoard
print("Puzzle Initialised!")

print("\n############PREPROCESSING PUZZLE############")
proPuzzleBoard = pp.preProcess(puzzleBoard) #Calls function in preprocessing.py
print("Puzzle preprocessed")

print("\n############SETTING INITIAL PRIORITIES############")
proPuzzleBoard = sp.setPriorities(proPuzzleBoard) #Calls function in set_priority.py
print("Priorities set")

print("\n############CREATING GRAPH############")
globalNodeList = gr.createGraph(proPuzzleBoard) #Calls function in graph.py
print("Graph Created")

print("\n############STARTING ACO############") #All functions called are in ACO.py
ACO.setProbability(globalNodeList, 0)
initialPuzzleBoard = createInitialCopy(proPuzzleBoard)
#writeBoardStateToCSV(initialPuzzleBoard, "cell")

proPuzzleBoard, currentPath = ACO.startACO(initialPuzzleBoard, proPuzzleBoard, globalNodeList, 0)
print("ACO Done probably")




















#~~~~~~~~~~~~~~Just outputs and stuff~~~~~~~~~~~~~~~~~
print("\n \n \n")
print("#####CELL#####")
outputBoard(proPuzzleBoard, "cell")
print("#####LIT#####")
outputBoard(proPuzzleBoard, "lit")
print("#####LIGHTABLE#####")
outputBoard(proPuzzleBoard, "lightable")
print("#####PRIORITY#####")
outputBoard(proPuzzleBoard, "priority")
print("#####INITIAL#####")
outputBoard(initialPuzzleBoard, "cell")
print("\n\n\n")

writeBoardStateToCSV(proPuzzleBoard, "cell")
writeBoardStateToCSV(proPuzzleBoard, "lit")
writeBoardStateToCSV(proPuzzleBoard, "lightable")
writeBoardStateToCSV(proPuzzleBoard, "priority")







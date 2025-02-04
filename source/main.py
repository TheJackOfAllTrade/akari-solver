import preprocessing as pp


class Cell: #Each cell in the puzzle board and its attributes
    def __init__(self, cellType, lit, lightable):
        self.cellType = cellType
        self.lit = lit #This is whether a cell is lit by a lightbulb or not
        self.lightable = lightable #Don't be fooled, "Lightable" in this case means a cell can't have a lightbulb. I'm just dumb and too lazy to change it

    def placeBulb(self, board, x, y):

        directions = ["up","down","left","right"]
        for i in directions:
            stopped = False
            yCoord = y
            xCoord = x
            while not stopped:
                if board[yCoord][xCoord].cellType == "-" or board[yCoord][xCoord].cellType == "L": 
                    if i == "up":
                        board[yCoord][xCoord].lit = True
                        if yCoord <= 0:
                            stopped = True
                        else:
                            yCoord -= 1
                    elif i == "down":
                        print(str(yCoord))
                        board[yCoord][xCoord].lit = True
                        if yCoord >= (len(board) - 1):
                            stopped = True
                        else:
                            yCoord += 1
                    elif i == "left":
                        board[yCoord][xCoord].lit = True
                        if xCoord <= 0:
                            stopped = True
                        else:
                            xCoord -= 1
                    elif i == "right":
                        board[yCoord][xCoord].lit = True
                        if xCoord >= (len(board[0]) - 1):
                            stopped = True
                        else:    
                            xCoord += 1
                    else:
                        print("OOOOOOO SCHOOOBIDY LOOBIDY!!")
                else:
                    print("Met Cell type [" + board[yCoord][xCoord].cellType + "]. Moving on...")
                    stopped = True
        return board

def readFile(): #Reads the file and formats each cell into the Cell object, adding them to the puzzleBoard array
    file = open("puzzles/7x7-6", "r")
    content = file.readlines()

    for i in content[7:(len(content)-1)]:
        currentLine = []
        for x in i:
            if x == " " or repr(x) == repr("\n"):
                next
            elif x == "-":
                newCell = Cell(x, False, True)
                currentLine.append(newCell)
            else:
                newCell = Cell(x, False, False)
                currentLine.append(newCell)
        puzzleBoard.append(currentLine)
    file.close()

def outputBoard(puzzleBoard, type):
    if type == "cell":
        for y in range(len(puzzleBoard)):
            line = []
            for x in range(len(puzzleBoard[y])):
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
    else:
        print("Not a valid output type")

puzzleBoard = [] #The initial puzzleboard, a 2D array of "Cell" Objects
readFile() #Initialises puzzleBoard
print("Puzzle Initialised!")

proPuzzleBoard = pp.preProcess(puzzleBoard) #Calls function in preprocessing.py
print("Puzzle preprocessed")


outputBoard(proPuzzleBoard, "cell")
outputBoard(proPuzzleBoard, "lit")

#for i in range(len(proPuzzleBoard)):
#    print("##########################")
#    print(proPuzzleBoard[i][5].cellType)
#    print(proPuzzleBoard[i][5].lit)





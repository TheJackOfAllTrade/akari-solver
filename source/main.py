import preprocessing as pp


class Cell: #Each cell in the puzzle board and its attributes
    def __init__(self, cellType, lit, lightable):
        self.cellType = cellType
        self.lit = lit #This is whether a cell is lit by a lightbulb or not
        self.lightable = lightable #Don't be fooled, "Lightable" in this case means a cell can't have a lightbulb. I'm just dumb and too lazy to change it

    def placeBulb(self, board, xCoord, yCoord):
        directions = ["up","down","left","right"]
        for i in directions:
            while (yCoord >= 0) or (yCoord <= len(board)) or (xCoord >= 0) or (xCoord <= len(board[0])):
                if i == "up":
                    print(str(yCoord))
                    board[yCoord][xCoord].lit = True
                    yCoord -= 1
                elif i == "down":
                    board[y+1][x].lit = True
                    y += 1
                elif i == "left":
                    board[y][x-1].lit = True
                    x -= 1
                elif i == "right":
                    board[y][x+1].lit = True
                    x += 1
                else:
                    print("OOOOOOO SCHOOOBIDY LOOBIDY!!")
        return board

def readFile(): #Reads the file and formats each cell into the Cell object, adding them to the puzzleBoard array
    file = open("akari-solver/puzzles/7x7-6", "r")
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





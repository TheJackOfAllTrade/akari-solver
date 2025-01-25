import preprocessing as pp


class Cell: #Each cell in the puzzle board and its attributes
    def __init__(self, cellType, lit, lightable):
        self.cellType = cellType
        self.lit = lit
        self.lightable = lightable

def readFile(): #Reads the file and formats each cell into the Cell object, adding them to the puzzleBoard array
    file = open("akari-solver/puzzles/7x7-2", "r")
    content = file.readlines()

    for i in content[7:(len(content)-1)]:
        currentLine = []
        for x in i:
            if x == "\n":
                next
            else:
                if x == "-":
                    newCell = Cell(x, False, True)
                else:
                    newCell = Cell(x, False, False)
                currentLine.append(newCell)
        puzzleBoard.append(currentLine)
        

    file.close()


puzzleBoard = [] #The initial puzzleboard, a 2D array of "Cell" Objects
readFile() #Initialises puzzleBoard
print("Puzzle Initialised!")

proPuzzleBoard = pp.preProcess(puzzleBoard) #Calls function in preprocessing.py
print("Puzzle preprocessed")

print(puzzleBoard[1][0].lightable)
print(proPuzzleBoard[1][0].lightable)


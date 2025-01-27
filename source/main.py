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


puzzleBoard = [] #The initial puzzleboard, a 2D array of "Cell" Objects
readFile() #Initialises puzzleBoard
print("Puzzle Initialised!")
print(repr(puzzleBoard[1][1].cellType))

proPuzzleBoard = pp.preProcess(puzzleBoard) #Calls function in preprocessing.py
print("Puzzle preprocessed")

print(proPuzzleBoard[0][2].lightable)    # For the case of
print(proPuzzleBoard[0][1].lightable)    #    - - -
print(proPuzzleBoard[1][0].lightable)    #    - 0 -
print(proPuzzleBoard[1][2].lightable)    #    - - -
print(proPuzzleBoard[2][1].lightable)    # Testing Purposes (Expected: True False False False False)


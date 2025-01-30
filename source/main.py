import preprocessing as pp


class Cell: #Each cell in the puzzle board and its attributes
    def __init__(self, cellType, lit, lightable):
        self.cellType = cellType
        self.lit = lit #This is whether a cell is lit by a lightbulb or not
        self.lightable = lightable #Don't be fooled, "Lightable" in this case means a cell can't have a lightbulb. I'm just dumb and too lazy to change it

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


puzzleBoard = [] #The initial puzzleboard, a 2D array of "Cell" Objects
readFile() #Initialises puzzleBoard
print("Puzzle Initialised!")

proPuzzleBoard = pp.preProcess(puzzleBoard) #Calls function in preprocessing.py
print("Puzzle preprocessed")

for i in range(len(proPuzzleBoard)):
    print("##########################")
    print(proPuzzleBoard[i][5].cellType)
    print(proPuzzleBoard[i][5].lit)





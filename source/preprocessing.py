


def preProcess(puzzleBoard): #What is called in the main
    processedPuzzleBoard = puzzleBoard #Doesn't overwrite puzzleBoard just in case
    processedPuzzleBoard = lookForZero(processedPuzzleBoard)
    processedPuzzleBoard = lookForFour(processedPuzzleBoard)
    return processedPuzzleBoard

def lookForZero(processedPuzzleBoard): #Searches the board for any cells containing a zero
    for y in range(len(processedPuzzleBoard)):
        for x in range(len(processedPuzzleBoard[y])):
            if processedPuzzleBoard[y][x].cellType == "0":
                print("Found 0 at (" + str(x) + "," + str(y) + ")")
                processedPuzzleBoard = setZero(processedPuzzleBoard, x, y)
            else:
                next
    return processedPuzzleBoard

def lookForFour(processedPuzzleBoard): #Searches the board for any cells containing a four
    for y in range(len(processedPuzzleBoard)):
        for x in range(len(processedPuzzleBoard[y])):
            if processedPuzzleBoard[y][x].cellType == "4":
                print("Found 4 at (" + str(x) + "," + str(y) + ")")
                processedPuzzleBoard = setFour(processedPuzzleBoard, x, y)
            else:
                next
    return processedPuzzleBoard

def setZero(puzzleBoard, x , y): #Sets surrounding cells as unlightable
    processedPuzzleBoard = puzzleBoard
    if (x <= 0): #If the 0 is on the left of the board
        processedPuzzleBoard[y][x+1].lightable = False
        processedPuzzleBoard[y+1][x].lightable = False
        processedPuzzleBoard[y-1][x].lightable = False
    if (x >= len(processedPuzzleBoard[y])): #If the 0 is on the right of the board
        processedPuzzleBoard[y][x-1].lightable = False
        processedPuzzleBoard[y+1][x].lightable = False
        processedPuzzleBoard[y-1][x].lightable = False
    if (y <= 0): #If the 0 is on the top of the board
        processedPuzzleBoard[y][x+1].lightable = False
        processedPuzzleBoard[y][x-1].lightable = False
        processedPuzzleBoard[y+1][x].lightable = False
    if (y >= len(processedPuzzleBoard)): #If the 0 is on the bottom of the board
        processedPuzzleBoard[y][x+1].lightable = False
        processedPuzzleBoard[y][x-1].lightable = False
        processedPuzzleBoard[y-1][x].lightable = False
    else: #Set all adjacent tiles to unlightable
        processedPuzzleBoard[y][x+1].lightable = False
        processedPuzzleBoard[y][x-1].lightable = False
        processedPuzzleBoard[y+1][x].lightable = False
        processedPuzzleBoard[y-1][x].lightable = False
    return processedPuzzleBoard

def setFour(puzzleBoard, x, y):
    processedPuzzleBoard = puzzleBoard
    
    #Places a lightbulb at each adjacent cell then calls the placeBulb function to light all relevant cells
    #try:
    catchx = x+1
    catchy = y
    catchdirection = "right"
    processedPuzzleBoard[y][x+1].cellType = "L"
    processedPuzzleBoard = processedPuzzleBoard[y][x+1].placeBulb(processedPuzzleBoard, x+1, y)

    catchx = x-1
    catchy = y
    catchdirection = "left"
    processedPuzzleBoard[y][x-1].cellType = "L"
    #processedPuzzleBoard = processedPuzzleBoard[y][x-1].placeBulb(processedPuzzleBoard, x-1, y)

    catchx = x
    catchy = y+1
    catchdirection = "down"
    processedPuzzleBoard[y+1][x].cellType = "L"
    #processedPuzzleBoard = processedPuzzleBoard[y+1][x].placeBulb(processedPuzzleBoard, x, y+1)
    
    catchx = x
    catchy = y-1
    catchdirection = "up"
    processedPuzzleBoard[y-1][x].cellType = "L"
    #processedPuzzleBoard = processedPuzzleBoard[y-1][x].placeBulb(processedPuzzleBoard, x, y-1)
    
    #except IndexError:
        #print("Tried to place a lightbulb outside the gameboard like an idiot at " + str(catchx) + " " + str(catchy) + " in the " + catchdirection + " direction")
    
    #finally:
    return processedPuzzleBoard



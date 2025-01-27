


def preProcess(puzzleBoard): #What is called in the main
    processedPuzzleBoard = puzzleBoard #Doesn't overwrite puzzleBoard just in case
    processedPuzzleBoard = lookForZero(processedPuzzleBoard)
    return processedPuzzleBoard

def lookForZero(processedPuzzleBoard): #Searches the board for any cells containing a zero
    for y in range(len(processedPuzzleBoard)):
        for x in range(len(processedPuzzleBoard[y])):
            if processedPuzzleBoard[y][x].cellType == "0":
                print("Setting (" + str(x) + "," + str(y) + ")")
                processedPuzzleBoard = setZero(processedPuzzleBoard, x, y)
            else:
                next
    return processedPuzzleBoard

def setZero(puzzleBoard, x , y): #Sets surrounding cells as unlightable
    processedPuzzleBoard = puzzleBoard
    if (x <= 0): #If the 0 is on the left of the board
        processedPuzzleBoard[y][x+1].lightable = False
        processedPuzzleBoard[y+1][x].lightable = False
        processedPuzzleBoard[y-1][x].lightable = False
    elif (x >= len(processedPuzzleBoard[y])): #If the 0 is on the right of the board
        processedPuzzleBoard[y][x-1].lightable = False
        processedPuzzleBoard[y+1][x].lightable = False
        processedPuzzleBoard[y-1][x].lightable = False
    elif (y <= 0): #If the 0 is on the top of the board
        processedPuzzleBoard[y][x+1].lightable = False
        processedPuzzleBoard[y][x-1].lightable = False
        processedPuzzleBoard[y+1][x].lightable = False
    elif (y >= len(processedPuzzleBoard)): #If the 0 is on the bottom of the board
        processedPuzzleBoard[y][x+1].lightable = False
        processedPuzzleBoard[y][x-1].lightable = False
        processedPuzzleBoard[y-1][x].lightable = False
    else: #Set all adjacent tiles to unlightable
        processedPuzzleBoard[y][x+1].lightable = False
        processedPuzzleBoard[y][x-1].lightable = False
        processedPuzzleBoard[y+1][x].lightable = False
        processedPuzzleBoard[y-1][x].lightable = False
    return processedPuzzleBoard

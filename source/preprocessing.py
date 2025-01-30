


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
    try:
        processedPuzzleBoard[y][x+1].cellType = "L"
        processedPuzzleBoard = placeBulb(processedPuzzleBoard, x+1, y, "right")

        processedPuzzleBoard[y][x-1].cellType = "L"
        processedPuzzleBoard = placeBulb(processedPuzzleBoard, x-1, y, "left")

        processedPuzzleBoard[y+1][x].cellType = "L"
        processedPuzzleBoard = placeBulb(processedPuzzleBoard, x, y+1, "down")
        
        processedPuzzleBoard[y-1][x].cellType = "L"
        processedPuzzleBoard = placeBulb(processedPuzzleBoard, x, y-1, "left")

    except IndexError:
        print(str(x) + " " + str(y))
        print("Tried to place a lightbulb outside the gameboard like an idiot")
    
    return processedPuzzleBoard

def placeBulb(puzzleBoard, x, y, direction):
    stopped = False
    print("Place Bulb called")
    while not stopped:
        print("Started Looping")
        if direction == "right": #Keeps going right until hits either the edge of the board or another type of cell (e.g another number or blocked cell)
            x += 1
            if x <= len(puzzleBoard[y]):
                print("Not out of bounds")
                if puzzleBoard[y][x].cellType == "-":
                    print("Changing cell (" + str(x) + "," + str(y) + ") to lit")
                    puzzleBoard[y][x].lit = True
                else:
                    stopped = True
            else:
                stopped = True
        elif direction == "left": #Keeps going left until hits either the edge of the board or another type of cell (e.g another number or blocked cell)
            x -= 1
            if x >= 0:
                if puzzleBoard[y][x].cellType == "-":
                    print("Changing cell (" + str(x) + "," + str(y) + ") to lit")
                    puzzleBoard[y][x].lit = True
                else:
                    stopped = True
            else:
                stopped = True
        elif direction == "up": #Keeps going up until hits either the edge of the board or another type of cell (e.g another number or blocked cell)
            y -= 1
            if y >= 0:
                if puzzleBoard[y][x].cellType == "-":
                    print("Changing cell (" + str(x) + "," + str(y) + ") to lit")
                    puzzleBoard[y][x].lit = True
                else:
                    stopped = True
            else:
                stopped = True
        elif direction == "down": #Keeps going down until hits either the edge of the board or another type of cell (e.g another number or blocked cell)
            y += 1
            if y <= len(puzzleBoard):
                if puzzleBoard[y][x].cellType == "-":
                    print("Changing cell (" + str(x) + "," + str(y) + ") to lit")
                    puzzleBoard[y][x].lit = True
                else:
                    stopped = True
            else:
                stopped = True
        else:
            print("Something has gone horribly wrong in the set light function")
        return puzzleBoard



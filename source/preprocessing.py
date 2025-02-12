


def preProcess(puzzleBoard): #What is called in the main
    processedPuzzleBoard = puzzleBoard #Doesn't overwrite puzzleBoard just in case
    processedPuzzleBoard = lookForZero(processedPuzzleBoard)
    processedPuzzleBoard = lookForFour(processedPuzzleBoard)
    processedPuzzleBoard = lookForRest(processedPuzzleBoard)
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

def lookForRest(processedPuzzleBoard):
    for y in range(len(processedPuzzleBoard)):
        for x in range(len(processedPuzzleBoard[y])):
            if processedPuzzleBoard[y][x].cellType == "3" or processedPuzzleBoard[y][x].cellType == "2" or processedPuzzleBoard[y][x].cellType == "1":
                print("Found " + processedPuzzleBoard[y][x].cellType + " at (" + str(x) + "," + str(y) + ")")
                processedPuzzleBoard = dealWithRest(processedPuzzleBoard, x, y)
            else:
                next
    return processedPuzzleBoard


def setZero(puzzleBoard, x , y): #Sets surrounding cells as unlightable
    processedPuzzleBoard = puzzleBoard
    try:
        processedPuzzleBoard[y][x+1].lightable = 0
        processedPuzzleBoard[y][x-1].lightable = 0
        processedPuzzleBoard[y+1][x].lightable = 0
        processedPuzzleBoard[y-1][x].lightable = 0
    except IndexError:
        print()
    finally:
        return processedPuzzleBoard

def setFour(puzzleBoard, x, y):
    processedPuzzleBoard = puzzleBoard
    
    #Places a lightbulb at each adjacent cell then calls the placeBulb function to light all relevant cells
    try:
        catchx = x+1
        catchy = y
        catchdirection = "right"
        #processedPuzzleBoard[y][x+1].cellType = "L"
        processedPuzzleBoard = processedPuzzleBoard[y][x+1].placeBulb(processedPuzzleBoard, x+1, y)

        catchx = x-1
        catchy = y
        catchdirection = "left"
        #processedPuzzleBoard[y][x-1].cellType = "L"
        processedPuzzleBoard = processedPuzzleBoard[y][x-1].placeBulb(processedPuzzleBoard, x-1, y)

        catchx = x
        catchy = y+1
        catchdirection = "down"
        #processedPuzzleBoard[y+1][x].cellType = "L"
        processedPuzzleBoard = processedPuzzleBoard[y+1][x].placeBulb(processedPuzzleBoard, x, y+1)
        
        catchx = x
        catchy = y-1
        catchdirection = "up"
        #processedPuzzleBoard[y-1][x].cellType = "L"
        processedPuzzleBoard = processedPuzzleBoard[y-1][x].placeBulb(processedPuzzleBoard, x, y-1)

    
    except IndexError:
        print("Tried to place a lightbulb outside the gameboard like an idiot at " + str(catchx) + " " + str(catchy) + " in the " + catchdirection + " direction")
    
    finally:
        return processedPuzzleBoard

def dealWithRest(puzzleBoard, x, y):
    if(puzzleBoard[y][x].cellType == "3"):
        surroundings = countSurroundings(puzzleBoard, x, y)
        print("There are " + str(surroundings) + " valid cells around (" + str(x) + "," + str(y) + ")")
    elif(puzzleBoard[y][x].cellType == "2"):
        print("Hmm...Yes, this is a 2")
    elif(puzzleBoard[y][x].cellType == "1"):
        print("Hmm...Yes, this is a 1")
    else:
        print("Hmm...I have no clue what this is.")
    
    return puzzleBoard

def countSurroundings(puzzleBoard, x, y):
    count = 0
    directions = ["up", "down", "left", "right"]
    for i in directions:
        try:
            if i == "up":
                cell = puzzleBoard[y-1][x]
                if (y-1 >= 0) and cell.cellType == "-" and cell.lit == 0 and cell.lightable == 1:
                    count += 1
                else:
                    next
            elif i == "down":
                cell = puzzleBoard[y+1][x]
                if (y+1 <= len(puzzleBoard)) and cell.cellType == "-" and cell.lit == 0 and cell.lightable == 1:
                    count += 1
                else:
                    next
            elif i == "left":
                cell = puzzleBoard[y][x-1]
                if (x-1 >= 0) and cell.cellType == "-" and cell.lit == 0 and cell.lightable == 1:
                    count += 1
                else:
                    next
            elif i == "right":
                cell = puzzleBoard[y][x+1]
                if (x+1 <= len(puzzleBoard[0])) and cell.cellType == "-" and cell.lit == 0 and cell.lightable == 1:
                    count += 1
                else:
                    next
        except IndexError:
                next
    return count

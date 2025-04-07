

def setPriorities(puzzleBoard):
    puzzleBoard = resetPriority(puzzleBoard)

    for y in range(len(puzzleBoard)):
        for x in range(len(puzzleBoard[0])):

            directions = ["up","down","left","right"]
            for i in directions:
                try:
                    #print("Checking " + i)
                    if i == "up":
                        cell = puzzleBoard[y-1][x]
                    elif i == "down":
                        cell = puzzleBoard[y+1][x]
                    elif i == "left":
                        cell = puzzleBoard[y][x-1]
                    elif i == "right":
                        cell = puzzleBoard[y][x+1]
                    else:
                        print("ERROR: Directionally blind in SetPriorities")
                except IndexError:
                    #print("OUT OF BOUNDS!!!")
                    continue
        
                if cell.cellType == "3" or cell.cellType == "2" or cell.cellType == "1":
                    puzzleBoard[y][x].priority += int(cell.cellType)
                    #print("Cell (" + str(x) + "," + str(y) + ")'s priority is now " + str(puzzleBoard[y][x].priority) + " through a +Cell")

            if puzzleBoard[y][x].cellType != "-" or puzzleBoard[y][x].lit == 1 or puzzleBoard[y][x].lightable == 0:
                puzzleBoard[y][x].priority = 0
            else:
                puzzleBoard[y][x].priority += 1 
                #print("Cell (" + str(x) + "," + str(y) + ")'s priority is now " + str(puzzleBoard[y][x].priority) + " through a +1")

    return puzzleBoard

def resetPriority(puzzleBoard):
    for y in range(len(puzzleBoard)):
        for x in range(len(puzzleBoard[0])):
            puzzleBoard[y][x].priority = 0

    return puzzleBoard
    
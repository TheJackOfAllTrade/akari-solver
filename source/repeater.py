import main
import datetime

elapsedTimes = []
solvedSolutions = 0

def calculateDeltaTime(start, end):
    deltaTime = end - start
    return deltaTime.total_seconds()

try:
    for i in range(100):
        print("Current Iteration: ", i)
        startTime = datetime.datetime.now()
        solved = main.main(puzzleBoard=[], proPuzzleBoard=[], globalNodeList=[])
        endTime = datetime.datetime.now()
        deltaTime = calculateDeltaTime(startTime, endTime)
        if solved:
            solvedSolutions += 1
            elapsedTimes.append(deltaTime)
            print("Iteration ", i, " Runtime: ", deltaTime)
        else:
            elapsedTimes.append(deltaTime)
            print("Iteration ", i, " Runtime: ", deltaTime)
except KeyboardInterrupt:
    avgRuntime = sum(elapsedTimes)/i+1
else:
    avgRuntime = sum(elapsedTimes)/100


if not elapsedTimes:
    print("\n\n\n\n====================================================================================")
    print("No solutions made")
    print("====================================================================================\n\n\n\n")
else:
    print("\n\n\n\n====================================================================================")
    print("Average Runtime: ", avgRuntime)
    print("Amount of times solved (/100): ", solvedSolutions)
    print("====================================================================================\n\n\n\n")

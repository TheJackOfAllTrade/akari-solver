def function(number, number2):
    number2 += 1
    if number == 10:
        return True, number2
    else:
        return False, number2
    
numCheck, numPlusOne = function(10, 15)
print(numCheck)
print(numPlusOne)
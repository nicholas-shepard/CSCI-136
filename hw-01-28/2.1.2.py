def odd(bool1, bool2, bool3):
    trueCounter = 0
    if bool1 == True:
        trueCounter += 1
    if bool2 == True:
        trueCounter += 1
    if bool3 == True:
        trueCounter += 1
        
    if (trueCounter % 2 == 0):
        return False
    else:
        return True

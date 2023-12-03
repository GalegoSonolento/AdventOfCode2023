sumTot = 0

numThreeLetter = {"one": "1", "two": "2", "six": "6"}
numFourLetter = {"four": "4", "five": "5", "nine": "9"}
numFiveLetter = {"three": "3", "seven": "7", "eight": "8"}
lettersDict = {0: numThreeLetter, 1: numFourLetter, 2: numFiveLetter}

while True:
    inp = input()

    if inp == "":
        break

    num = ""
    numToTot = 0

    foundExtendedPos = -1
    foundExtendedPos5 = 999
    foundExtendedPos4 = 999
    foundExtendedPos3 = 999
    numExtended = ""
    numExtended5 = ""
    numExtended4 = ""
    numExtended3 = ""
    windowRange = 6
    brekar = False
    for i in range(2, -1, -1):
        windowRange -= 1
        for j in range(0, len(inp)):
            if brekar:
                brekar = False
                break
            if j + windowRange <= len(inp):
                for k in lettersDict[i]:
                    currentTxt = inp[j:j + windowRange]
                    if inp[j:j + windowRange] == k:
                        if windowRange == 5:
                            numExtended5 = lettersDict[i][k]
                            foundExtendedPos5 = j
                            brekar = True
                        elif windowRange == 4:
                            numExtended4 = lettersDict[i][k]
                            foundExtendedPos4 = j
                            brekar = True
                        elif windowRange == 3:
                            numExtended3 = lettersDict[i][k]
                            foundExtendedPos3 = j
                            brekar = True
    if foundExtendedPos5 < foundExtendedPos4 and foundExtendedPos5 < foundExtendedPos3:
        numExtended = numExtended5
        foundExtendedPos = foundExtendedPos5
    elif foundExtendedPos4 < foundExtendedPos5 and foundExtendedPos4 < foundExtendedPos3:
        numExtended = numExtended4
        foundExtendedPos = foundExtendedPos4
    elif foundExtendedPos3 < foundExtendedPos5 and foundExtendedPos3 < foundExtendedPos4:
        numExtended = numExtended3
        foundExtendedPos = foundExtendedPos3

    numeric = ""
    foundNumericPos = 999
    for i, j in enumerate(inp):
        if j.isnumeric():
            numeric += j
            foundNumericPos = i
            break

    if foundExtendedPos < foundNumericPos:
        num += numExtended
    else:
        num += numeric

    foundExtendedPos = -1
    foundExtendedPos5 = -1
    foundExtendedPos4 = -1
    foundExtendedPos3 = -1
    numExtended = ""
    numExtended5 = ""
    numExtended4 = ""
    numExtended3 = ""
    windowRange = 6
    brekar = False
    for i in range(2, -1, -1):
        windowRange -= 1
        for j in range(len(inp), -1, -1):
            if brekar:
                brekar = False
                break
            if j + windowRange <= len(inp):
                for k in lettersDict[i]:
                    currentTxt = inp[j:j + windowRange]
                    if inp[j:j + windowRange] == k:
                        if windowRange == 5:
                            numExtended5 = lettersDict[i][k]
                            foundExtendedPos5 = j
                            brekar = True
                        elif windowRange == 4:
                            numExtended4 = lettersDict[i][k]
                            foundExtendedPos4 = j
                            brekar = True
                        elif windowRange == 3:
                            numExtended3 = lettersDict[i][k]
                            foundExtendedPos3 = j
                            brekar = True
    if foundExtendedPos5 > foundExtendedPos4 and foundExtendedPos5 > foundExtendedPos3:
        numExtended = numExtended5
        foundExtendedPos = foundExtendedPos5
    elif foundExtendedPos4 > foundExtendedPos5 and foundExtendedPos4 > foundExtendedPos3:
        numExtended = numExtended4
        foundExtendedPos = foundExtendedPos4
    elif foundExtendedPos3 > foundExtendedPos5 and foundExtendedPos3 > foundExtendedPos4:
        numExtended = numExtended3
        foundExtendedPos = foundExtendedPos3

    numeric = ""
    foundNumericPos = -1
    for i in range(len(inp) - 1, -1, -1):
        if inp[i].isnumeric():
            numeric += inp[i]
            foundNumericPos = i
            break

    if foundExtendedPos > foundNumericPos:
        num += numExtended
    else:
        num += numeric

    if len(num) == 1:
        num += num[0]
    numToTot = int(num)
    sumTot += numToTot

print(sumTot)

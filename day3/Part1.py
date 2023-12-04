with open("input.txt", "r") as infile:
    input = infile.readlines()

inputDict = {}
for i, j in enumerate(input):
    inputDict[i] = j

def findInteger(i, j):
    number = ""
    initPos = -1
    takeAway = 1
    while True:
        if j-takeAway >= 0:
            if not inputDict[i][j-takeAway].isnumeric():
                initPos = j - takeAway + 1
                break
        else:
            initPos = 0
            break
        takeAway += 1
    for k in range(initPos, len(inputDict[i])):
        if inputDict[i][k].isnumeric():
            number += inputDict[i][k]
        else:
            break
    return int(number)


sumTot = 0
numberPlacement = 0
# Precisa criar algum tipo de regra pra ir tirando os números daqui, um contador até 3 pra tirar o último, ir retirando
# conforme passa, contar até 2, sla
previousNum = []
currentNum = 0
for i in inputDict:
    for j in range(0, len(inputDict[i])):
        if not inputDict[i][j].isnumeric() and not inputDict[i][j] == ".":
            if i - 1 >= 0:
                if j - 1 >= 0:
                    if inputDict[i-1][j-1].isnumeric():
                        currentNum = findInteger(i - 1, j - 1)
                        if currentNum not in previousNum:
                            previousNum.append(currentNum)
                            sumTot += currentNum
                if j >= 0:
                    if inputDict[i-1][j].isnumeric():
                        currentNum = findInteger(i - 1, j)
                        if currentNum not in previousNum:
                            previousNum.append(currentNum)
                            sumTot += currentNum
                if j + 1 < len(inputDict[i-1]):
                    if inputDict[i-1][j+1].isnumeric():
                        currentNum = findInteger(i - 1, j + 1)
                        if currentNum not in previousNum:
                            previousNum.append(currentNum)
                            sumTot += currentNum
            if i >= 0:
                if j - 1 >= 0:
                    if inputDict[i][j-1].isnumeric():
                        currentNum = findInteger(i, j - 1)
                        if currentNum not in previousNum:
                            previousNum.append(currentNum)
                            sumTot += currentNum
                # if j >= 0:
                #     if inputDict[i][j].isnumeric():
                #         sumTot += findInteger(i, j)
                if j + 1 < len(inputDict[i]):
                    if inputDict[i][j+1].isnumeric():
                        currentNum = findInteger(i, j + 1)
                        if currentNum not in previousNum:
                            previousNum.append(currentNum)
                            sumTot += currentNum
            if i + 1 < len(inputDict):
                if j - 1 >= 0:
                    if inputDict[i+1][j-1].isnumeric():
                        currentNum = findInteger(i + 1, j - 1)
                        if currentNum not in previousNum:
                            previousNum.append(currentNum)
                            sumTot += currentNum
                if j > 0 and j < len(inputDict[i+1]):
                    if inputDict[i+1][j].isnumeric():
                        currentNum = findInteger(i + 1, j)
                        if currentNum not in previousNum:
                            previousNum.append(currentNum)
                            sumTot += currentNum
                if j+1 < len(inputDict[i+1]):
                    if inputDict[i+1][j+1].isnumeric():
                        currentNum = findInteger(i + 1, j + 1)
                        if currentNum not in previousNum:
                            previousNum.append(currentNum)
                            sumTot += currentNum



for i in range(0, len(inputDict)):
    print(inputDict[i])

print(sumTot)
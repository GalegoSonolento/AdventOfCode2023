with open("input.txt", "r") as infile:
    input = infile.readlines()

totPoints = 0

for inp in input:
    startRead = False
    rightNum = []
    luckyNum = []
    luckyRead = False
    firstPass = True
    currentPointScore = 0
    inp = str(input())
    if inp == "":
        break

    for i in inp.split():
        if i[len(i)-1] == ":":
            startRead = True
        if startRead:
            if i.isnumeric():
                if luckyRead:
                    luckyNum.append(i)
                else:
                    rightNum.append(i)
            if i == "|":
                luckyRead = True

    for i in luckyNum:
        if i in rightNum:
            if firstPass:
                currentPointScore += 1
                firstPass = False
            else:
                currentPointScore *= 2

    totPoints += currentPointScore

print(totPoints)
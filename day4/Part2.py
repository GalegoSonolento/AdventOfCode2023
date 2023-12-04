countRows = 0
allCardsQtde = {}

while True:
    countRows += 1
    inp = str(input())
    if inp == "":
        break

    if countRows in allCardsQtde:
        allCardsQtde[countRows] += 1
    else:
        allCardsQtde[countRows] = 1

    for z in range(0, allCardsQtde[countRows]):
        nextCardsQuan = 0
        startRead = False
        rightNum = []
        luckyNum = []
        luckyRead = False

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
                nextCardsQuan += 1

        for i in range(countRows+1, countRows+nextCardsQuan+1):
            if i in allCardsQtde:
                allCardsQtde[i] += 1
            else:
                allCardsQtde[i] = 1
            
cardsCounter = 0
for i in range(1, len(allCardsQtde)+1):
    cardsCounter += allCardsQtde[i]

print(cardsCounter)
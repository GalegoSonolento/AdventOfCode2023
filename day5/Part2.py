with open("input.txt", "r") as infile:
    input = infile.readlines()

dictList = {}
seedRead = True
anteriorCheck = ""
actualCheck = ""
intervalsList = []
lowest = -999

# pra parte 2 precisa mudar só algumas coisas dentro dessa parte do código aqui
# pra testar com input direto do terminal dá pra tirar as linhas em branco do input mesmo e jogar aqui, aí uso meu
# procedimento padrão de encerrar na linha em branco

for i, j in enumerate(input):
    if i > 0:
        break
    for k in range(1, len(j.split())):
        intervalsList.append(int(j.split()[k]))

for l in range(0, len(intervalsList), 2):
    start = intervalsList[l]
    finish = start + intervalsList[l+1] - 1
    for p in range(start, finish):


        for i in input:
            if len(i) > len('\n'):
                if seedRead:
                    seedRead = False
                    dictList["seed"] = p
                    actualCheck = "seed"
                    #for n in range(1, len(i.split()), 2):
                        # startRange = int(i.split()[n])
                        # seedRange = int(i.split()[n+1])
                        # for r in range(startRange, startRange+seedRange):
                        #     dictList.append({"seed": int(r)})
                        #     actualCheck = "seed"

                else:
                    if not i[0].isnumeric():
                        dictList[i.split()[0].split("-")[2]] = -1
                        anteriorCheck = actualCheck
                        actualCheck = i.split()[0].split("-")[2]
                    elif i[0].isnumeric:
                        values = i.split()
                        for v in range(0, len(values)):
                            helper = values[v]
                            values[v] = int(helper)
                        if dictList[anteriorCheck] in range(values[1], values[1]+values[2]):
                            calc = dictList[anteriorCheck] - values[1]
                            dictList[actualCheck] = values[0] + calc
                        else:
                            if dictList[actualCheck] < 0 or dictList[actualCheck] == dictList[anteriorCheck]:
                                dictList[actualCheck] = dictList[anteriorCheck]
        seedRead = True
        if lowest == -999:
            lowest = dictList['location']
        elif dictList['location'] < lowest:
            lowest = dictList['location']


print(lowest)
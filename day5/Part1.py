with open("input.txt", "r") as infile:
    input = infile.readlines()

dictList = []
seedRead = True
anteriorCheck = ""
actualCheck = ""

# pra parte 2 precisa mudar só algumas coisas dentro dessa parte do código aqui
# pra testar com input direto do terminal dá pra tirar as linhas em branco do input mesmo e jogar aqui, aí uso meu
# procedimento padrão de encerrar na linha em branco
for i in input:
    if len(i) > len('\n'):
        if seedRead:
            seedRead = False
            for j, k in enumerate(i.split()):
                if j > 0:
                    dictList.append({"seed": int(k)})
            actualCheck = "seed"
        else:

            if not i[0].isnumeric():
                for d in dictList:
                    d[i.split()[0].split("-")[2]] = -1
                anteriorCheck = actualCheck
                actualCheck = i.split()[0].split("-")[2]
            elif i[0].isnumeric:
                for d in dictList:
                    values = i.split()
                    for v in range(0, len(values)):
                        values[v] = int(values[v])
                    if d[anteriorCheck] in range(values[1], values[1]+values[2]):
                        calc = d[anteriorCheck] - values[1]
                        d[actualCheck] = values[0] + calc
                    else:
                        if d[actualCheck] < 0 or d[actualCheck] == d[anteriorCheck]:
                            d[actualCheck] = d[anteriorCheck]

lowest = 0
for k, i in enumerate(dictList):
    if k == 0:
        lowest = i['location']
    if i['location'] < lowest:
        lowest = i['location']

print(lowest)
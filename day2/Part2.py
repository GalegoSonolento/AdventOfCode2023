with open("input.txt", "r") as infile:
    input = infile.readlines()

sumPowers = 0
for i in input:
    power = 1
    colorsDict = {"red": 0, "green": 0, "blue": 0}
    test = int(i.split()[1].split(":")[0])

    color = ""
    qtdeColor = -1
    for j in range(2, len(i.split()), 2):
        qtdeColor = int(i.split()[j].split(":")[0])
        color = i.split()[j+1].split(",")[0].split(";")[0]
        if qtdeColor > colorsDict[color]:
            colorsDict[color] = qtdeColor
    for j, k in enumerate(colorsDict):
        power = power * colorsDict[k]
        print(power)
    sumPowers += power

print(sumPowers)
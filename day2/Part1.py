with open("input.txt", "r") as infile:
    input = infile.readlines()


colorsDict = {"red": 12, "green": 13, "blue": 14}

sumPossibilities = 0
for i in input:
    test = int(i.split()[1].split(":")[0])
    sumPossibilities += int(i.split()[1].split(":")[0])
    color = ""
    qtdeColor = -1
    for j in range(2, len(i.split()), 2):

        qtdeColor = int(i.split()[j].split(":")[0])
        color = i.split()[j+1].split(",")[0].split(";")[0]
        if qtdeColor > colorsDict[color]:
            sumPossibilities -= int(i.split()[1].split(":")[0])
            break

print(sumPossibilities)
sumTot = 0

while True:
    inp = str(input())

    if inp == "":
        break

    num = ""
    for i in inp:
        if i.isnumeric():
            num += i
            break
    for i in range(len(inp)-1, -1, -1):
        if inp[i].isnumeric():
            num += inp[i]
            break
    if len(num) == 1:
        num += num[0]
    numInt = int(num)
    sumTot += numInt

print(sumTot)
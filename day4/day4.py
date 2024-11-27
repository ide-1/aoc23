with open("input.txt") as file:
    input = file.read()
    input = input.splitlines()

for i in range(len(input)):
    line = input[i].split(': ')
    line[1] = line[1].split(' | ')
    #print(line[1])
    for j in range(len(line[1])):
        part = line[1][j]
        part = part.split(' ')
        for p in part:
            if p == '':
                part.remove('')
        line[1][j] = part
    for p in range(len(line[1])):
        pa = line[1][p]
        for n in range(len(pa)):
            pa[n] = int(pa[n])
        line[1][p] = pa
    input[i] = line
#print(input)

tot = 0

for card in input:
    winNums = card[1][0]
    myNums = card[1][1]
    cardpoints = 0
    for num in myNums:
        if num in winNums:
            if cardpoints == 0:
                cardpoints = 1
            else: cardpoints *= 2
    tot += cardpoints

print(tot)
copies = [0] * len(input)
for c in range(len(input)):
    copies[c] += 1
    card = input[c]
    winNums = card[1][0]
    myNums = card[1][1]
    cardwins= 0
    for num in myNums:
        if num in winNums:
            cardwins +=1

    for cop in range(c+1, c+cardwins+1):
        print('iteration', cop)
        print('last nummer' ,copies[c])
        copies[cop] = copies[cop] + copies[c]
        print(copies)
print(copies)
print(sum(copies))
        
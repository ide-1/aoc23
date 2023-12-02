with open("input.txt") as file:
    input = file.read()
    input = input.splitlines()

for i in range(len(input)): 
    line = input[i]
    line = line.split(': ')
    line[0] = int("".join(line[0].split("Game ")))
    line[1] = line[1].split('; ')
    for p in range(len(line[1])):
        pull = line[1][p]
        pull = pull.split(', ')
        for c in range(len(pull)):
            color = pull[c] 
            color = color.split(' ')
            color[0] = int(color[0])
            pull[c] = color

       # pull = tuple(pull.split(' '))
        line[1][p] = pull


    input[i] = line
    print(line)

#print(input)

tot = 0
for game in input:
    possible = True
    for pull in game[1]:
        for color in pull:
            if (color[0] > 12 and color[1] == 'red') or (color[0] > 13 and color[1] == 'green') or (color[0] > 14 and color[1] == 'blue'):
                possible = False
                break
    if possible:
        tot += game[0]

print(tot)

sum = 0
for game in input:
    red = 0
    blue = 0
    green = 0
    for pull in game[1]:
        for color in pull:
            if color[1] == 'red' and color[0] > red:
                red = color[0]
            
            elif color[1] == 'blue' and color[0] > blue:
                blue = color[0]
            
            elif color[1] == 'green' and color[0] > green:
                green = color[0]
    power = red * blue * green
    sum += power

print(sum)
with open("input.txt") as file:
    input = file.read()
    input = input.splitlines()

for i in range(len(input)):
    input[i] = list(input[i])
    


sum = 0
for i in range(1, len(input)):
    for j in range(1, len(input[i])):
        if  not input[i][j].isdigit() or input[i][j] != '.':
            one = input[i-1][j-1]
            two = input[i-1][j]
            three = input[i-1][j+1]
            four = input[i][j-1]
            five = input[i][j+1]
            six = input[i+1][j-1]
            seven = input[i+1][j]
            eight = input[i+1][j+1]
            
            
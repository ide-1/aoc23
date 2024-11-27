with open("input.txt") as file:
    input = file.read()
    input = input.split('\n\n')


seeds = input[0].split(' ')
seeds.pop(0)
for s in range(len(seeds)):
    seeds[s] = int(seeds[s])

seedsoil = {}
soilfert = {}
fertwater = {}
waterlight = {}
lighttemp = {}
temphum = {}
humloc = {}

for i in range(1, len(input)):
    map = input[i].splitlines()
    map.pop(0)
    for l in map: 
        l = l.split(' ')
        if i == 1:
            seedsoil[l[1]] = (int(l[0]), int(l[2]))
        elif i == 2:
            soilfert[l[1]] = (int(l[0]), int(l[2]))
        elif i == 3:
            fertwater[l[1]] = (int(l[0]), int(l[2]))
        elif i == 4:
            waterlight[l[1]] = (int(l[0]), int(l[2]))
        elif i == 5:
            lighttemp[l[1]] = (int(l[0]), int(l[2]))
        elif i == 6:
            temphum[l[1]] = (int(l[0]), int(l[2]))
        elif i == 7:
            humloc[l[1]] = (int(l[0]), int(l[2]))
        else: break

locs = []
for s in seeds:
    for key in seedsoil:
        if int(key) <= s <= seedsoil[key][1]+ int(key):
            next = seedsoil[key]
            for i in soilfert:
                if int(i) <= next[0] <= soilfert[i][1]+ int(key):
                    next = 
                    for j
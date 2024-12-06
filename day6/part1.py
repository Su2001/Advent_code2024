map = []
with open("input.txt") as fin:
    map_s = fin.read().strip().split("\n")
    for i, row in enumerate(map_s):
        temp = []
        for j, elem in enumerate(row):
            if elem == ".":
                temp.append(0)
            elif elem == "#":
                temp.append(-1)
            else:
                temp.append(1)
                pos = (i,j)
        map.append(temp)

import numpy as np

def process(map:list[int], init:tuple[int, int]):
    m = np.array(map)
    dirs = [(-1,0), (0,1), (1,0), (0, -1)]
    ini = 0
    x, y = init
    try:
        while True:
            tempx = x + dirs[ini][0]
            tempy = y + dirs[ini][1]
            if m[tempx, tempy] == -1:
                ini = (ini + 1) % 4
                continue
            x = tempx
            y = tempy
            m[x, y] = 1
    except:
        return (m == 1).sum()

    

print(process(map, pos))





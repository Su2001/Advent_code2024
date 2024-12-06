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
    visited = set()
    dirs = [(-1,0), (0,1), (1,0), (0, -1)]
    dir = 0
    x, y = init
    try:
        while True:
            tempx = x + dirs[dir][0]
            tempy = y + dirs[dir][1]
            if m[tempx, tempy] == -1:
                dir = (dir + 1) % 4
                continue
            x, y = tempx, tempy
            visited.add((x,y))
            m[x, y] = 1
    except:
        return visited
    
def hasLoop(init, m):
    localx, localy = init[0], init[1]
    dirs = [(-1,0), (0,1), (1,0), (0, -1)]
    dir = 0
    visits = set()
    while True:
        if (localx, localy, dir) in visits:
            return 1
        visits.add((localx, localy, dir))

        nextx = localx + dirs[dir][0]
        nexty = localy + dirs[dir][1]

        if not (0 <= nextx < len(m) and 0 <= nexty < len(m)):
            return 0

        if m[nextx, nexty] == -1:
            dir = (dir + 1) % 4
            continue
        localx, localy = nextx, nexty

ans = 0
m = np.array(map)
for x, y in process(map, pos):
    if m[x][y] == -1:
        continue
    m[x,y] = -1
    ans += hasLoop(pos, m) 
    m[x, y] = 0

print(ans)
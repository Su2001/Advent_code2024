from itertools import combinations, product
signals = {}
with open("input.txt") as fin:
    datas = fin.read().strip().split("\n")
    for i, row in enumerate(datas):
        for j, c in enumerate(row): 
            if c != '.':
                if c not in signals:
                    signals[c] = [(i,j)]
                else:
                    signals[c].append((i,j))
n = len(datas)

def in_bounds(x, y):
    return 0 <= x < n and 0 <= y < n

def antinodes(a, b):
    ax, ay = a
    bx, by = b
    sx, sy = bx - ax, by - ay
    tempx, tempy = ax, ay
    while in_bounds(tempx, tempy):
        yield (tempx, tempy)
        tempx, tempy = tempx - sx, tempy - sy   

    tempx, tempy = bx, by
    while in_bounds(tempx, tempy):
        yield (tempx, tempy)
        tempx, tempy = tempx + sx, tempy + sy 

result = set()
for _, signal in signals.items():
    for a, b in combinations(signal, r=2):
        for antinode in antinodes(a, b):
            result.add(antinode)

print(len(result))

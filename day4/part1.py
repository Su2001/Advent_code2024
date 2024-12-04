with open("input.txt") as fin:
    data = fin.read().strip().split("\n")

n = len(data)
m = len(data[0])

directions = []
for x in range(-1, 2):
    for y in range(-1, 2):
        if x != 0 or y != 0:
            directions.append((x, y))

def find_xmas(i, j, direction):
    x, y = direction
    for k, target in enumerate("XMAS"):
        posx = i + k * x
        posy = j + k * y
        if not (0 <= posx < n and 0 <= posy < m):
            return 0
        if data[posx][posy] != target:
            return 0
    return 1

ans = 0
for i in range(n):
    for j in range(m):
        for d in directions:
            ans += find_xmas(i, j, d)

print(ans)


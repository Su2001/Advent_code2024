with open("input.txt") as fin:
    data = fin.read().strip().split("\n")

n = len(data)
m = len(data[0])

def find_xmas(x, y):
    if data[x][y] != "A":
        return 0

    diag_1 = f"{data[i-1][j-1]}{data[i+1][j+1]}"
    diag_2 = f"{data[i-1][j+1]}{data[i+1][j-1]}"

    return 1 if diag_1 in ["MS", "SM"] and diag_2 in ["MS", "SM"] else 0

ans = 0
for i in range(1, n-1):
    for j in range(1, m-1):
        ans += find_xmas(i, j)

print(ans)


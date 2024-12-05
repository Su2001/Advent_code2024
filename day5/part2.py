with open("input.txt") as fin:
    raw_rules, updates = fin.read().strip().split("\n\n")
    rules = {}
    unique = []
    for line in raw_rules.split("\n"):
        a, b = list(map(int,line.split("|")))
        if a not in rules:
            rules[a] = [b]
        else:
            rules[a].append(b)
        if b not in unique:
            unique.append(b)
    updates = [list(map(int, line.split(","))) for line in updates.split("\n")]
for i in unique:
    if i not in rules:
        rules[i] = []

ans = []

def fixError(update:list[int], pos: int):
    currect = update.copy()
    while True:
        no_error = True
        for i in range(pos, len(update) - 1):
            if currect[i] in rules[currect[i+1]]:
                no_error = False
                currect[i], currect[i+1] = currect[i+1], currect[i]
        if no_error:
            return currect[int(len(update)/2)]

def process(update:list[int]):
    for i in range(len(update)-1):
        t = update[i]
        for elem in update[i:]:
            if t in rules[elem]:
                return False, i
    return True, 0

for update in updates:
    r = process(update)
    if r[0]:
        continue

    ans.append(fixError(update, r[1]))

print(sum(ans))



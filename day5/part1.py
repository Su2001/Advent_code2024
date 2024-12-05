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

def process(update:list[int]):
    for i in range(len(update)-1):
        t = update[i]
        for elem in update[i:]:
            if t in rules[elem]:
                return 0
    return update[int(len(update)/2)]

for update in updates:
    ans.append(process(update))

print(sum(ans))



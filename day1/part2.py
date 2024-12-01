with open("input.txt") as fin:
    data = fin.read()

ans = 0
a = []
b = {}

for line in data.strip().split("\n"):
    nums = [int(i) for i in line.split("   ")]
    a.append(nums[0])
    if nums[1] not in b:
        b[nums[1]] = 1
    else:
        b[nums[1]] += 1

c = [i * b.setdefault(i,0) for i in a]

print(sum(c))
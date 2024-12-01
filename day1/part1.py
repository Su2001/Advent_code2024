with open("input.txt") as fin:
    data = fin.read()

ans = 0
a = []
b = []

for line in data.strip().split("\n"):
    nums = [int(i) for i in line.split("   ")]
    a.append(nums[0])
    b.append(nums[1])

a.sort()
b.sort()

c = [ abs(i - j) for i,j in zip(a,b)]

print(sum(c))
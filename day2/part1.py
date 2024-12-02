with open("input.txt") as fin:
    data = fin.read()

ans = 0
a = []
b = []

def isSafe(nums:list[int]):
    temp = [[],[]]
    flag = 0
    for i,j in zip(nums[:-1],nums[1:]):
        dif = i-j
        if dif < 0:
            temp[0].append(1)
        else:
            temp[1].append(1)
        if abs(dif) < 1 or abs(dif) > 3 or (len(temp[0]) != 0 and len(temp[1]) != 0) :
            flag = 1
            break
    if flag == 0:
        return 1
    return 0

for line in data.strip().split("\n"):
    nums = [int(i) for i in line.split(" ")]
    ans += isSafe(nums)

print(ans)


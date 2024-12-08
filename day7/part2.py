from itertools import product

from tqdm import tqdm


with open("input.txt") as fin:
    datas = fin.read().strip().split("\n")

ans = 0
for i, line in tqdm(enumerate(datas)):
    parts = line.split()
    value = int(parts[0][:-1])
    nums = list(map(int, parts[1:]))

    def check(combo, value):
        ans = nums[0]
        for i in range(1, len(nums)):
            if combo[i-1] == "+":
                ans += nums[i]
            elif combo[i-1] == "*":
                ans *= nums[i]
            else:
                ans = int(f"{ans}{nums[i]}")
            if ans > value:
                return -1
        return ans

    for combo in product("*+|", repeat=len(nums)-1):
        if check(combo, value) == value:
            ans += value
            break

print(ans)
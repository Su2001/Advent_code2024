import re

with open("input.txt") as fin:
    data = fin.read().strip()

ans = 0
nums = re.findall(r"mul\((\d+),(\d+)\)", data)
    
for i in nums:
    ans += int(i[0]) * int(i[1])

print(ans)


import re

with open("input.txt") as fin:
    data = fin.read().strip()

ans = 0
nums = re.findall(r"mul\((\d+),(\d+)\)|(do\(\)|don't\(\))", data)
flag = 1
    
for i in nums:
    if "do()" in i:
        flag = 1
    elif "don't()" in i:
        flag = 0
    elif flag:
        ans += int(i[0]) * int(i[1])

print(ans)
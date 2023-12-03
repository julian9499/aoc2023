import re

f = open("files/day3.txt")

OFFSET = 100000

grid = [[y for y in x.strip()] for x in f.readlines()]

# for x in grid:
#     print(x)

nums = []
numsPerLine = []
starRegs = {}
starNums = []

for i,x in enumerate(grid):
    for j,y in enumerate(x):
        if y == '*':
            starRegs[i+j*OFFSET] = []

for i,x in enumerate(grid):
    numbers = re.findall("[0-9]+","".join(x))
    sub_length = [len(x) for x in numbers]
    total_length = len("".join(numbers))
    it = 0
    checks = []
    numsPerLine.append(0)

    for j,y in enumerate(x):
        if re.match("[0-9]", y):
            it += 1
            check = []
            for gx in range(i-1, i+2):
                for gy in range(j-1, j+2):
                    if 0 <= gx < len(x) and 0 <= gy < len(x):
                        if "*".find(grid[gx][gy]) == 0:
                            check.append(gx+gy*OFFSET)
            checks.append(check)

        if it == total_length:
            break
    ind = 0
    for p,k in enumerate(sub_length):
        for coord in set(sum(checks[ind:ind+k],[])):
            starRegs[coord].append(int(numbers[p]))
        ind +=k

ans = 0
for l in starRegs.values():
    if len(l) == 2:
        ans += l[0] * l[1]

print(ans)
# print(starRegs)
# print(sum(nums))
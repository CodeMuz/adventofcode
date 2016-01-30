#!/usr/bin/python

with open("input.txt") as f:
    content = f.readlines()

grid = []

i = 0
# Read the numbers from the input file into array
for line in content:
    grid.append([])
    grid[i] = []
    line = line.replace("\n", "")
    for c in line:
        if c == '.':
            grid[i].append(0)
        if c == '#':
            grid[i].append(1)
    i = i + 1

runtime = 100

def calcLightPosition(currentLight, neighbours):
    if (currentLight == 1):
        if (neighbours == 2 or neighbours == 3):
            value = 1
        else:
            value = 0
    else:
        if (neighbours == 3):
            value = 1
        else:
            value = 0
    return value


for _ in range(runtime):
    scratch = []
    for x in range(len(grid)):
        scratch.append([])
        for y in range(len(grid[x])):

            scratch[x].append([])

            if 0 <= x - 1 < len(grid):
                top = grid[x - 1][y]
            else:
                top = 0
            if 0 <= x + 1 < len(grid):
                bottom = grid[x + 1][y]
            else:
                bottom = 0
            if 0 <= y + 1 < len(grid[x]):
                right = grid[x][y + 1]
            else:
                right = 0
            if 0 <= y - 1 < len(grid[x]):
                left = grid[x][y - 1]
            else:
                left = 0

            if 0 <= x - 1 < len(grid) and 0 <= y - 1 < len(grid[x]):
                topleft = grid[x - 1][y - 1]
            else:
                topleft = 0

            if 0 <= x - 1 < len(grid) and 0 <= y + 1 < len(grid[x]):
                topright = grid[x - 1][y + 1]
            else:
                topright = 0

            if 0 <= x + 1 < len(grid) and 0 <= y - 1 < len(grid[x]):
                bottomleft = grid[x + 1][y - 1]
            else:
                bottomleft = 0

            if 0 <= x + 1 < len(grid) and 0 <= y + 1 < len(grid[x]):
                bottomright = grid[x + 1][y + 1]
            else:
                bottomright = 0

            result = top + right + left + bottom + topleft + topright + bottomleft + bottomright

            scratch[x][y] = calcLightPosition(grid[x][y], result)

    for x in range(len(grid)):
        for y in range(len(grid[x])):
            grid[x][y] = scratch[x][y]

total = 0
for x in range(len(grid)):
    for y in range(len(grid[x])):
        if (grid[x][y]):
            total = total + 1

print total

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


def calcLightPosition(currentLight, neighbours):
    if (currentLight == 1):
        value = 1 if (neighbours == 2 or neighbours == 3) else 0
    else:
        value = 1 if (neighbours == 3) else 0
    return value

def setCornersOn(grid):
    grid[0][0] = 1
    grid[height - 1][0] = 1
    grid[0][len(grid[0]) - 1] = 1
    grid[height - 1][len(grid[0]) - 1] = 1
    return grid

runtime = 100
height = len(grid)
width = len(grid[0])
for _ in range(runtime):
    grid = setCornersOn(grid)
    scratch = []
    for x in range(height):
        scratch.append([])
        for y in range(width):
            scratch[x].append([])
            r = 0
            r += grid[x - 1][y] if 0 <= x - 1 < height else 0
            r += grid[x + 1][y] if 0 <= x + 1 < height else 0
            r += grid[x][y + 1] if 0 <= y + 1 < width else 0
            r += grid[x][y - 1] if 0 <= y - 1 < width else 0
            r += grid[x - 1][y - 1] if 0 <= x - 1 < height and 0 <= y - 1 < width else 0
            r += grid[x - 1][y + 1] if 0 <= x - 1 < height and 0 <= y + 1 < width else 0
            r += grid[x + 1][y - 1] if 0 <= x + 1 < height and 0 <= y - 1 < width else 0
            r += grid[x + 1][y + 1] if 0 <= x + 1 < height and 0 <= y + 1 < width else 0

            scratch[x][y] = calcLightPosition(grid[x][y], r)

    for x in range(height):
        for y in range(width):
            grid[x][y] = scratch[x][y]

    grid = setCornersOn(grid)

total = 0
for x in range(height):
    for y in range(width):
        if (grid[x][y]):
            total = total + 1

print total

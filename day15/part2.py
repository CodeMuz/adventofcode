#!/usr/bin/python

category = ['capacity','durability','flavor','texture','calories']

n = []
i = [0, 0, 0, 0]
max = 100

with open("input.txt") as f:
    content = f.readlines()

ingredients = {}
for line in content:
    line = line.replace(",", "").replace(":", "").split(' ')
    ingredients[line[0]] = {
        'capacity': int(line[2]),
        'durability': int(line[4]),
        'flavor': int(line[6]),
        'texture': int(line[8]),
        'calories': int(line[10])

    }

for a in range(max):
    i[0] = a
    for b in range(max):
        i[1] = b
        if i[0] + b >= max:
            break
        for c in range(max):
            i[2] = c
            if (i[0] + i[1] + i[2]) >= max:
                break
            else:
                i[3] = max - (i[0] + i[1] + i[2])
                n.append(list(i))

def calcPerm(p):

    t = {'capacity': 0,
     'durability': 0,
     'flavor': 0,
     'texture': 0,
     'calories': 0}

    for c in category:
        j = 0
        for o in ingredients:
            t[c] += p[j] * ingredients[o][c]
            j += 1

    total = 1
    for v in t:
        if v == 'calories':
            if t[v] != 500:
                total = 0
        else:
            if t[v] < 0:
                t[v] = 0
            total *= t[v]

    return total

best = 0

for x in n:
    result = calcPerm(x)
    if result > best:
        best = result

print best
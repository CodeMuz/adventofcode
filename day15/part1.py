#!/usr/bin/python

with open("input.txt") as f:
    content = f.readlines()

ingredients = {}
for line in content:
    line = line.replace(",", "").replace(":", "").split(' ')
    ingredients[line[0]] = {
        'capacity': int(line[2]),
        'durability': int(line[4]),
        'flavor': int(line[6]),
        'texture': int(line[8])
    }

# n = []
# i = [0, 0, 0, 0]
# max = 100

# Generate all pairs adding to 100
# for a in range(max):
#     i[0] = a
#     for b in range(max):
#         i[1] = b
#         if i[0] + b >= max:
#             break
#         for c in range(max):
#             i[2] = c
#             if (i[0] + i[1] + i[2]) >= max:
#                 break
#             else:
#                 i[3] = max - (i[0] + i[1] + i[2])
#                 n.append(list(i))

n = []
i = [0, 0]
max = 100

for a in range(max):
    i[0] = a
    i[1] = max - a
    n.append(list(i))

print n


# for k in n:
#     print k

best = 0
value = {'capacity': 0,
         'durability': 0,
         'flavor': 0,
         'texture': 0
         }

print (len(ingredients))
for x in n:

    for i in ingredients:

        for category in ingredients[i]:

            for pos in range(len(x)):
                print pos
                value[category] += (x[pos] * ingredients[i][category])

    total = value['capacity'] * value['durability'] * value['flavor'] * value['texture']


    value = {'capacity': 0,
         'durability': 0,
         'flavor': 0,
         'texture': 0
         }

    if total >= best:
        best = total

print best

        # value = {'capacity': 0,
        #          'durability': 0,
        #          'flavor': 0,
        #          'texture': 0,
        #          'calories': 0
        #          }
        # print total

        # print ingredients

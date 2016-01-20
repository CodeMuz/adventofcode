#!/usr/bin/python

output = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

with open("input.txt") as f:
    content = f.readlines()


# cat and tree greater than
# pomeranians and goldfish less than

def isMatch(prop):
    for v in prop:
        if v == 'cats' or v == 'trees':
            if prop[v] <= output[v]:
                return False
            continue
        if v == 'pomeranians' or v == 'goldfish':
            if prop[v] >= output[v]:
                return False
            continue
        if prop[v] != output[v]:
            return False

    return True


for line in content:
    lineArray = line.replace(",", "").replace(":", "").replace("\n", "").split(' ')
    number = lineArray[1]
    prop = {}
    prop[lineArray[2]] = int(lineArray[3])
    prop[lineArray[4]] = int(lineArray[5])
    prop[lineArray[6]] = int(lineArray[7])
    if isMatch(prop):
        print number

# print isMatch(prop)

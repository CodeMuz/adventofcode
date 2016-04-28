#!/usr/bin/python

from collections import defaultdict
data_dict = defaultdict(list)


with open("input.txt") as f:
    content = f.readlines()


# Read the numbers from the input file into array
replacements = 1
r = {}
for line in content:

    lineArray = line.replace(",", "").replace(":", "").replace("\n", "").split(' ')

    if(replacements == 1):
        if(lineArray[0] and lineArray[2]):
            data_dict[lineArray[0]].append(lineArray[2])
    else:
        string = lineArray

    if(len(line) == 1):
        replacements = 0

print data_dict
print string

outputs = []
for rep in data_dict:
    
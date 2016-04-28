#!/usr/bin/python

with open("input.txt") as f:
    content = f.readlines()


# Read the numbers from the input file into array
replacements = 1
r = {}
for line in content:

    lineArray = line.replace(",", "").replace(":", "").replace("\n", "").split(' ')
    print lineArray

    if(replacements):
        r[lineArray[0]] = lineArray[2]
    if(line == ''):
        replacements = 0
        r[lineArray[0]] = lineArray[2]

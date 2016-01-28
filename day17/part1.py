#!/usr/bin/python
import itertools
import sys

with open("input.txt") as f:
    content = f.readlines()

numbers = []

# Read the numbers from the input file into array
for line in content:
    line = line.replace("\n", "")
    numbers.append(int(line))

print numbers
stuff = numbers
i = 0
value = 150
totalCount = 0
for L in range(0, len(stuff) + 1):
    for subset in itertools.combinations(stuff, L):
        # print subset
        t = 0
        itemIndex = 0
        stopCounting = False
        for i in subset:
            itemIndex += 1
            if(stopCounting == True):
                break
            t += i
            if t > value:
                stopCounting = True
            elif t == value and itemIndex == len(subset):
                totalCount += 1
                stopCounting = True

print totalCount
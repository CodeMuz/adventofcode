#!/usr/bin/python

with open("input.txt") as f:
    content = f.readlines()

numbers = []

# Read the numbers from the input file into array
for line in content:
    line = line.replace("\n","")
    numbers.append(int(line))

def findsets(list):
    sets = []
    for x in range(len(list)):
        for i in list:
            if i not in sets:
                sets.append(i)
    return sets

numbers = [1,2,3]

print(findsets(numbers))
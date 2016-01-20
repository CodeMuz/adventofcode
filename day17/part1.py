#!/usr/bin/python

with open("input.txt") as f:
    content = f.readlines()

numbers = []

# Read the numbers from the input file into array
for line in content:
    line = line.replace("\n","")
    numbers.append(int(line))


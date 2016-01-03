with open("input.txt") as f:
    content = f.readlines()

distances = {}
people = []
for line in content:
    line = line.split(' ')

    # Initialize variables
    personA = line[0]
    personB = line[10].split('.')[0]
    value = int(line[3])

    change = line[2]

    # Add new people
    if personA not in people:
        people.append(personA)
    if personB not in people:
        people.append(personB)

    if change == "lose":
        value = -value
    if personA not in distances:
        distances[personA] = {personB: value}
    else:
        node = distances[personA][personB] = value


happiness = 0

import itertools
p = itertools.permutations(people)
p = list(p)
# print len(p)
# print list(p[0])

for iter in p:
    personList = list(iter)
    print personList
    for person in personList:
        index = personList.index(person)
        if index != len(personList) - 1:
            nextPerson = index + 1
        else:
            nextPerson = 0
        personB = people[nextPerson]
        happiness += distances[person][personB]

print happiness
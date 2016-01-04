import itertools

with open("input.txt") as f:
    content = f.readlines()

distances = {}
people = []
H = 0

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

p = list(itertools.permutations(people))

for iter in p:

    happiness = 0

    personList = list(iter)

    for person in personList:
        index = personList.index(person)
        if index != (len(personList) - 1):
            nextPerson = index + 1
        else:
            nextPerson = 0
        personB = personList[nextPerson]
        happiness += distances[person][personB]
        happiness += distances[personB][person]

    if happiness > H:
        H = happiness

print H
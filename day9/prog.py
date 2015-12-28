with open("input.txt") as f:
    content = f.readlines()

nodes = ()
distances = {}
for line in content:
    line = line.split(' ')
    A = line[0];
    B = line[2];
    X = line[4].replace('\n','');
    if A not in nodes:
        nodes = nodes + (A,)

    if A in distances:
        dList = distances[A]
    else:
        dList = {}
    dList[B] = int(X)
    distances[A] = dList

for d in distances:
    print d
    print distances[d]
# unvisited = {node: None for node in nodes} #using None as +inf
# visited = {}
# current = 'Tristram'
# currentDistance = 0
# unvisited[current] = currentDistance
#
# while True:
#     for neighbour, distance in distances[current].items():
#         if neighbour not in unvisited: continue
#         newDistance = currentDistance + distance
#         if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
#             unvisited[neighbour] = newDistance
#     visited[current] = currentDistance
#     del unvisited[current]
#     if not unvisited: break
#     candidates = [node for node in unvisited.items() if node[1]]
#     current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]
#
# print(visited)
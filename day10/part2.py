def lookSay(code):
    cA = list(code)
    nC = {}
    j = 0
    s = ''
    x = 0
    for i in cA:
        if i in nC and nC[i] != 0:
            nC[i] += 1
        else:
            nC[i] = 1
        if (j != i) and (j != 0):
            s += reduce(lambda x, y: str(x) + str(y), [nC[j],j])
            nC[j] = 0
        if x == (len(cA) - 1):
            s += reduce(lambda x, y: str(x) + str(y), [nC[i],i])
        j = i
        x += 1
    return s

code = '1321131112'

for _ in range(50):
    code = lookSay(code)

print len(code)
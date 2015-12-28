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
            s += str(nC[j]) + str(j)
            nC[j] = 0
        if x == (len(cA) - 1):
            s += str(nC[i]) + str(i)
        j = i
        x += 1
    return s

code = '1321131112'

for _ in range(40):
    code = lookSay(code)

print len(code)
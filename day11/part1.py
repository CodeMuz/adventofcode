import string
values = dict()
reverseValues = dict()
for index, letter in enumerate(string.ascii_lowercase):
    values[letter] = index + 1
    reverseValues[index + 1] = letter

def stringToNumberList(list):
    for key,i in enumerate(list):
        list[key] = values[i]
    return list

def numberListToString(l):
    for key,i in enumerate(l):
        l[key] = reverseValues[i]
    return l

def increment(alist):
    rList = list(reversed(alist))
    for key,i in enumerate(rList):
        if i != 26:
            rList[key] += 1
            return list(reversed(rList))
        else:
            rList[key] = 1
    return list(reversed(rList))

# Passwords must include one increasing straight of at least three letters,
# like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
def containsStraight(l):
    for key,i in enumerate(l):
        if key == len(l) - 2:
            return False
        v1 = l[key]
        v2 = l[key + 1]
        v3 = l[key + 2]
        if (v1 + 1) == v2 and (v2 + 1) == v3:
            return True
    return False

# Passwords may not contain the letters i, o, or l,
# as these letters can be mistaken for other characters and are therefore confusing.
def doesNotContain(l):
    for i in l:
        if i in [values['i'],values['o'],values['l']]:
            return False
    return True

# Passwords must contain at least two different,
# non-overlapping pairs of letters, like aa, bb, or zz.
def containsPairs(l):
    p1 = ''
    for key,i in enumerate(l):
        if key == len(l) - 1:
            return False
        if l[key] == l[key + 1]:
            if p1 != '' and l[key] != p1:
                return True
            p1 = l[key]
    return False

input = 'hxbxwxba'

iList = list(input)
l = stringToNumberList(iList)

while (containsStraight(l) == False) or (doesNotContain(l) == False) or (containsPairs(l) == False):
    l = increment(l)

print ''.join(numberListToString(l))

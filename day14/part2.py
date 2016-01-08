#!/usr/bin/python

with open("input.txt") as f:
    content = f.readlines()

print content

rd = {}
for line in content:
    line = line.split(' ')
    rd[line[0]] = {
        'speed':int(line[3]),
        'duration':int(line[6]),
        'rest':int(line[13]),
        'distance':0,
        'points':0,
        'running':int(line[6]),
        'resttime':0,
        'resting':False
    }

def runRace(tick):

    while tick > 0:
        global rd

        for runner in rd:

            if rd[runner]['running'] > 0 and rd[runner]['resting'] == False:
                rd[runner]['distance'] += rd[runner]['speed']
                rd[runner]['running'] -= 1

            if rd[runner]['resting'] == True:
                rd[runner]['resttime'] -= 1

            if rd[runner]['running'] == 0 and rd[runner]['resting'] == False:
                rd[runner]['resting'] = True
                rd[runner]['resttime'] = rd[runner]['rest']

            if rd[runner]['resttime'] == 0 and rd[runner]['resting'] == True:
                rd[runner]['resting'] = False
                rd[runner]['running'] = rd[runner]['duration']

        winnerD = 0
        winnerRunner = ''

        jointWinners = []
        for runner in rd:
            if rd[runner]['distance'] > winnerD:
                winnerD = rd[runner]['distance']
                winnerRunner = runner
        for runner in rd:
            if rd[runner]['distance'] == winnerD and runner != winnerRunner:
                if len(jointWinners) == 0:
                    jointWinners.append(winnerRunner)
                    jointWinners.append(runner)
                else:
                    jointWinners.append(runner)
        if len(jointWinners) > 0:
            for runner in jointWinners:
                rd[runner]['points'] += 1
        else:
            rd[winnerRunner]['points'] += 1

        tick -= 1

tick = 2503

runRace(tick)

totalPoints = 0

for runner in rd:
    totalPoints += rd[runner]['points']
    print runner
    print rd[runner]['points']

print "Total is %d points" % (totalPoints)
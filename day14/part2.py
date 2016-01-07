#!/usr/bin/python

with open("input.txt") as f:
    content = f.readlines()

print content

rd = {}
for line in content:
    line = line.split(' ')
    rd[line[0]] = {'speed':line[3],'duration':line[6],'rest':line[13],'distance':0}

def calculateDistance(runner, tick):
    running = int(rd[runner]['duration'])
    resting = False
    resttime = 0
    print 'running: ' + runner
    while tick > 1:

        if running > 0 and resting == False:
            rd[runner]['distance'] += int(rd[runner]['speed'])
            running = running - 1

        if resting == True:
            resttime -= 1

        if running == 0 and resting == False:
            resting = True
            resttime = int(rd[runner]['rest'])

        if resttime == 0 and resting == True:
            resting = False
            running = int(rd[runner]['duration'])

        tick -= 1
    return rd[runner]['distance']

tick = 2503
for runner in rd:
    print calculateDistance(runner,tick)

#!/usr/bin/python

import thread
import time

with open("input.txt") as f:
    content = f.readlines()

print content

rd = {}
for line in content:
    line = line.split(' ')
    rd[line[0]] = {'speed':line[3],'duration':line[6],'rest':line[13],'updated':False,'distance':0}

print rd

tick = 2503

def master():
    global tick
    count = 0
    while tick != 0:
        count = 0
        for runner in rd:
            if rd[runner]['updated']:
                count += 1
        if count == len(rd):
            tick -= 1
            for runner in rd:
                rd[runner]['updated'] = False

    for runner in rd:
        print runner
        print rd[runner]['distance']

# Define a function for the thread
def run(runner):
    global tick
    running = rd[runner]['duration']
    resting = False
    resttime = 0
    print 'running thread' + runner
    while tick > 0:
        if rd[runner]['updated'] == False:
            if running > 0 and resting == False:
                rd[runner]['distance'] += rd[runner]['speed']
                running -= 1
            if running == 0:
                resting = True
                resttime = rd[runner]['rest']
            if resting == True:
                resttime -= 1
            if resting == 0:
                resting = False
            rd[runner]['updated'] = True

# Create two threads as follows
try:
    for runner in rd:
        print runner
        thread.start_new_thread( run, (runner) )
    thread.start_new_thread( master, () )
except:
   print "Error: unable to start thread"

while 1:
   pass
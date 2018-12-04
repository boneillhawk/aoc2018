from itertools import *
from functools import *
from copy import *
from collections import *
from heapq import *
from math import *
from hashlib import *
from datetime import *

f = open('input\\input4.txt', 'r')
data = [line.strip() for line in f.readlines()] # List of inputs
f.close()

class Info:
    def __init__(self, t, i):
        self.time = t
        self.message = i

    def __lt__(self,other):
        return self.time < other.time

    def __eq__(self,other):
        return self.time == other.time

def day4a(data):
    # Put input in chronological order
    infoset = []
    for line in data:
        year = int(line[1:5])
        month = int(line[6:8])
        day = int(line[9:11])
        hour = int(line[12:14])
        minute = int(line[15:17])
        message = line[19:]

        dt = datetime(year,month,day,hour,minute)
        
        infoset.append(Info(dt,message))

    ordered = sorted(infoset)

    # Process the input
    sleeptime = dict()
    current = -1
    start = 0
    for entry in ordered:
        if entry.message.startswith("Guard"):
            words = entry.message.split()
            current = int(words[1][1:])
            if current not in sleeptime:
                sleeptime[current] = [0]*60
        elif entry.message.startswith("falls"):
            start = entry.time.minute
        elif entry.message.startswith("wakes"):
            end = entry.time.minute
            for t in range(start, end):
                sleeptime[current][t] += 1

    # Identify sleepiest guard
    sleepiest = -1
    sleeptotal = 0
    for guard in sleeptime:
        if sum(sleeptime[guard]) > sleeptotal:
            sleepiest = guard
            sleeptotal = sum(sleeptime[guard])

    # Find the minute where the sleepiest guard slept most
    maxIdx = 0
    maxValue = sleeptime[sleepiest][0]
    for i in range(1,60):
        if sleeptime[sleepiest][i] > maxValue:
            maxIdx = i
            maxValue = sleeptime[sleepiest][i]

    return maxIdx * sleepiest

def day4b(data):
    # Put input in chronological order
    infoset = []
    for line in data:
        year = int(line[1:5])
        month = int(line[6:8])
        day = int(line[9:11])
        hour = int(line[12:14])
        minute = int(line[15:17])
        message = line[19:]

        dt = datetime(year,month,day,hour,minute)
        
        infoset.append(Info(dt,message))

    ordered = sorted(infoset)

    # Process the input
    sleeptime = dict()
    current = -1
    start = 0
    for entry in ordered:
        if entry.message.startswith("Guard"):
            words = entry.message.split()
            current = int(words[1][1:])
            if current not in sleeptime:
                sleeptime[current] = [0]*60
        elif entry.message.startswith("falls"):
            start = entry.time.minute
        elif entry.message.startswith("wakes"):
            end = entry.time.minute
            for t in range(start, end):
                sleeptime[current][t] += 1

    # Find the maximum entry in the entire dictionary of lists and which guard has it
    maxEntry = -1
    maxGuard = -1
    for guard in sleeptime:
        if max(sleeptime[guard]) > maxEntry:
            maxEntry = max(sleeptime[guard])
            maxGuard = guard

    # Find the location of that maximum in this guard's list
    for i in range(60):
        if sleeptime[maxGuard][i] == maxEntry:
            return i*maxGuard
            
        

print(day4a(data))
print(day4b(data))

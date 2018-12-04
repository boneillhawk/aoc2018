from itertools import *
from functools import *
from copy import *
from collections import *
from heapq import *
from math import *
from hashlib import *
import re

# Credit to Mike Hawes for the RE trick below
f = open('input\\input4.txt', 'r')
data = [re.findall("[\w]+", line) for line in f.readlines()] # List of inputs
f.close()

def day4(data):
    ordered = sorted(data)

    # Process the sorted input
    sleeptime = dict()
    current = -1
    start = 0
    for entry in ordered:
        word = entry[5]
        if word == "Guard":
            current = int(entry[6])
            if current not in sleeptime:
                sleeptime[current] = [0]*60
        elif word == "falls":
            start = int(entry[4])
        elif word == "wakes":
            end = int(entry[4])
            for t in range(start, end):
                sleeptime[current][t] += 1

    # Part A
    # Identify sleepiest guard
    sleepiest = -1
    sleepMax = 0
    for guard in sleeptime:
        if sum(sleeptime[guard]) > sleepMax:
            sleepiest = guard
            sleepMax = sum(sleeptime[guard])

    # Find the minute where the sleepiest guard slept most
    maxIdx = 0
    maxValue = sleeptime[sleepiest][0]
    for i in range(1,60):
        if sleeptime[sleepiest][i] > maxValue:
            maxIdx = i
            maxValue = sleeptime[sleepiest][i]

    partA = maxIdx * sleepiest

    # Part B
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
            partB = i*maxGuard
            break

    return partA, partB
            
print(day4(data))

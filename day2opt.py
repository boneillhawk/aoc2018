from itertools import *
from functools import *
from copy import *
from collections import *
from heapq import *
from math import *
from hashlib import *

f = open('input\\input2.txt', 'r')
data = [line.strip() for line in f.readlines()] # List of inputs
f.close()

def day2a(data):
    twos = 0
    threes = 0
    for line in data:
        dct = {}
        for ch in line:
            dct[ch] = dct.get(ch,0) + 1
        counts = dct.values()
        if 2 in counts:
            twos += 1
        if 3 in counts:
            threes += 1
    return twos*threes

def day2b(data):
    for x,y in combinations(data,2):
        diffIdx = -1
        found = False
        for ch in range(len(x)):
            if x[ch] != y[ch]:
                if diffIdx >= 0:
                    found = False
                    break
                else:
                    found = True
                    diffIdx = ch
        if found:
            return x[:diffIdx]+x[(diffIdx+1):]

print(day2a(data))
print(day2b(data))

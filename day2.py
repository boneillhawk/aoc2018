from itertools import *
from functools import *
from copy import *
from collections import *
from heapq import *
from math import *
from hashlib import *

f = open('input\\input2.txt', 'r')
data = [line.strip() for line in f.readlines()] # List of inputs
#data = f.readline().strip() # Single input
f.close()

def day2a(data):
    twos = 0
    threes = 0
    for line in data:
        dct = {}
        sawTwo = False
        sawThree = False
        for ch in line:
            dct[ch] = dct.get(ch,0) + 1
        for key in dct:
            if dct[key] == 2:
                sawTwo = True
            if dct[key] == 3:
                sawThree = True
        if sawTwo:
            twos += 1
        if sawThree:
            threes += 1
    return twos*threes

def day2b(data):
    for x,y in combinations(data,2):
        diffs = 0
        for ch in range(len(x)):
            if x[ch] != y[ch]:
                diffs += 1
            if diffs > 1:
                break
        if diffs == 1:
            return x,y

print(day2a(data))
print(day2b(data))

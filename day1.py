from itertools import *
from functools import *
from copy import *
from collections import *
from heapq import *
from math import *
from hashlib import *

f = open('input\\input1.txt', 'r')
data = [int(line.strip()) for line in f.readlines()] # List of inputs
f.close()

def day1a(data):
    return sum(data)

def day1b(data):
    total = 0
    visited = set()
    visited.add(0)
    for i in cycle(data):
        total += i
        if total in visited:
            return total
        visited.add(total)

print(day1a(data))
print(day1b(data))

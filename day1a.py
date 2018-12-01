import itertools
import functools
import copy
import collections
import heapq
import math
import hashlib
import sys

f = open('input\\input1.txt', 'r')
data = [int(line.strip()) for line in f.readlines()] # List of inputs
#data = f.readline().strip() # Single input
f.close()

total = 0
for i in data:
    total += i
print(total)

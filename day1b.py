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
visited = dict()
visited[0] = True
while True:
    for i in data:
        total += i
        if visited.get(total,False):
            print(total)
            sys.exit(0)
        visited[total] = True
#print(total)

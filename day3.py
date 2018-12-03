from itertools import *
from functools import *
from copy import *
from collections import *
from heapq import *
from math import *
from hashlib import *

f = open('input\\input3.txt', 'r')
data = [line.strip() for line in f.readlines()] # List of inputs
#data = f.readline().strip() # Single input
f.close()

def day3a(data):
    size = 1000
    fabric = [[0]*size for _ in range(size)]
    for line in data:
        parts = line.split()
        xy = parts[2].split(',')
        startx = int(xy[0])
        starty = int(xy[1][:-1])
        dims = parts[3].split('x')
        width = int(dims[0])
        height = int(dims[1])

        for x in range(startx,startx+width):
            for y in range(starty,starty+height):
                fabric[x][y] += 1

    count = 0
    for x in range(size):
        for y in range(size):
            if fabric[x][y] > 1:
                count += 1

    #print(fabric)
    return count

def day3b(data):
    fabric = [[None]*1000 for _ in range(1000)]
    allset = set(range(1,len(data)+1))
    for line in data:
        parts = line.split()
        fabid = int(parts[0][1:])
        xy = parts[2].split(',')
        startx = int(xy[0])
        starty = int(xy[1][:-1])
        dims = parts[3].split('x')
        width = int(dims[0])
        height = int(dims[1])

        for x in range(startx,startx+width):
            for y in range(starty,starty+height):
                if fabric[x][y] is None:
                    fabric[x][y] = fabid
                else:
                    allset -= set([fabric[x][y]])
                    allset -= set([fabid])


    return allset

print(day3a(data))
print(day3b(data))

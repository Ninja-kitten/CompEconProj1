# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 16:58:51 2017

@author: tran260
"""
import random
size = 3
grid = [[0 for j in range(size)] for i in range(size)]
path = 4
loc = [size//2,size//2]
grid[loc[0]][loc[1]]=1

for i in range(path):
    move = random.randint(0,3)
    if 0<loc[0]<size and 0<loc[1] < size: 
        if move == 0:
            loc[0] -= 1
        elif move == 1:
            loc [0] +=1
        elif move == 2:
            loc[1]-= 1
        elif move == 3:
            loc[1] += 1
        else:
            print("error")
    print(loc)
    grid[loc[0]][loc[1]] += 1
    print(grid)
print(all(grid[i][j]<=1 for i in range(size) for j in range(size)))
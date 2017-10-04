# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 10:54:03 2017

@author: tran260
"""
import matplotlib.pyplot as plt
import random

def choose_dir(loc,size,weight):
    #on the top or bottom row
    if loc[0] == 0 or loc[0]== size-1:
        #in a corner can do two moves
        if loc[1] == 0 or loc[1] == size-1:
            move = random.randint(0,1)
            if loc[0]==0:
                if move == 0:
                    loc[0] +=1
                    weight *= 1/2
                elif move == 1 and loc[1] == 0:
                    loc[1] +=1
                    weight *= 1/2
                elif move == 1 and loc[1] == size-1:
                    loc[1]-=1
                    weight *= 1/2
            elif loc[0] == size-1:
                if move == 0:
                    loc[0] -=1
                    weight *= 1/2
                elif move == 1 and loc[1] == 0:
                    loc[1] +=1
                    weight *= 1/2
                elif move == 1 and loc[1] == size-1:
                    loc[1]-=1
                    weight *= 1/2
                else:
                    print("error 1")
            else:
                print("error 2")
        #can do 3 moves on an edge
        else:
            move = random.randint(0,2)
            if move == 0 and loc[0]== 0:
                loc[0] += 1
                weight *= 1/3
            elif move == 0 and loc[0]==size-1:
                loc[0] -= 1
                weight *= 1/3
            elif move == 1:
                loc[1]-=1
                weight *= 1/3
            elif move == 2:
                loc[1] +=1
                weight *= 1/3
            else:
                print("error 3")
    #left or right edge
    elif loc[1] == 0 or loc[1] == size-1:
        move = random.randint(0,2)
        if move == 0 and loc[1]== 0:
            loc[1] += 1
            weight *= 1/3
        elif move == 0 and loc[1]==size-1:
            loc[1] -= 1
            weight *= 1/3
        elif move == 1:
            loc[0]-=1
            weight *= 1/3
        elif move == 2:
            loc[0] +=1
            weight *= 1/3
        else:
            print("error 4")
    else:
        move = random.randint(0,3)
        if move == 0:
            loc[0] -= 1
            weight *= 1/4
        elif move == 1:
            loc[0] += 1
            weight *= 1/4
        elif move == 2:
            loc[1] -= 1
            weight *= 1/4
        elif move ==3:
            loc[1] +=1
            weight *= 1/4
        else:
           print("error 5")    
    return loc,weight

def check_path(grid):
    size = len(grid)
    return all(grid[i][j]<=1 for i in range(size) for j in range(size))

def gen_path(size,length):
    grid = [[0 for j in range(size)] for i in range(size)]
    path = length
    loc = [size//2,size//2]
    grid[loc[0]][loc[1]]=1
    weight = 1
    for i in range(path):
        loc,weight = choose_dir(loc,size,weight)
        grid[loc[0]][loc[1]] +=1
        """plt.matshow(grid)
        plt.show()
        print(weight)"""
    valid_path = check_path(grid)
    return [valid_path,weight]

def trials_run(size,length,trials):
    sim_results = []
    for i in range(trials):
        sim_results.append(gen_path(size,length))
    weighted_paths = 0
    total_paths = 0
    for i in range(trials):
        weight = 1/sim_results[i][1]
        weighted_paths += sim_results[i][0]*weight
        total_paths+= sim_results[i][0]                
    return weighted_paths/total_paths
print(trials_run(3,4,1000))
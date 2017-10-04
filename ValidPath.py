# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 09:45:19 2017

@author: tran260
"""
import random

def gen_path(size,length):
    grid = [[0 for j in range(size)] for i in range(size)]
    path_length = length
    loc = [size//2,size//2]
    grid[loc[0]][loc[1]]=1
    path_prob = 1
    path_remaining = path_length
    for i in range(path_length):
        valid_moves = count_valid_moves(grid,loc,path_remaining)
        if valid_moves == 0:
            break
        else:
            path_prob *= 1/valid_moves
            move = gen_valid_move(grid,loc,path_remaining)
            grid = use_move(grid,move)
            loc = move
            path_remaining -=1
    
    validity = check_valid_path(grid,length)
    return [validity , path_prob]
    
def is_valid_move(grid,loc,move,length_remaining):
    size = len(grid)
    x, y = loc[0],loc[1]
    x_move,y_move = move[0]-loc[0],move[1]-loc[1]
    if x_move == -1:
        if x== 0:
            return False
        elif grid[x-1][y] == 1:
            return False
        elif count_empty_neighbors(grid,[x-1,y])== 0 and length_remaining!= 1:
            return False
    elif x_move == 1:
        if x== size-1:
            return False
        elif grid[x+1][y] == 1:
            return False
        elif count_empty_neighbors(grid,[x+1,y])== 0 and length_remaining!= 1:
            return False
    elif y_move == -1:
        if y == 0:
            return False
        elif grid[x][y-1] ==1:
            return False
        elif count_empty_neighbors(grid,[x,y-1])== 0 and length_remaining!= 1:
            return False
    elif y_move == 1:
        if y == size -1:
            return False
        elif grid[x][y+1] ==1:
            return False
        elif count_empty_neighbors(grid,[x,y+1])== 0 and length_remaining!= 1:
            return False
    else:
        print("invalid move")
        print(x_move)
        print(y_move)
        exit
    return True
        
def count_empty_neighbors(grid,loc):
    empty_neighbors = 4
    size = len(grid)
    x,y = loc[0],loc[1]
    if x == 0:
        empty_neighbors -=1
        empty_neighbors -= grid[x+1][y]
    elif x == size - 1:
        empty_neighbors -=1
        empty_neighbors -= grid[x-1][y]
    else:
        empty_neighbors -= grid[x+1][y]
        empty_neighbors -= grid[x-1][y]
    if y == 0:
        empty_neighbors -= 1
        empty_neighbors -= grid[x][y+1]
    elif y == size-1:
        empty_neighbors -= 1
        empty_neighbors -= grid[x][y-1]
    else:
        empty_neighbors -= grid[x][y+1]
        empty_neighbors -= grid[x][y-1]
    return empty_neighbors

def count_valid_moves(grid,loc,length_remaining):
    left = [loc[0]-1,loc[1]]
    right = [loc[0]+1,loc[1]]
    up = [loc[0],loc[1]+1]
    down = [loc[0],loc[1]-1]
    valid_moves = 0
    valid_moves += is_valid_move(grid,loc,left,length_remaining)
    valid_moves += is_valid_move(grid,loc,right,length_remaining)
    valid_moves += is_valid_move(grid,loc,up,length_remaining)
    valid_moves += is_valid_move(grid,loc,down,length_remaining)
    return valid_moves

def gen_valid_move(grid,loc,length_remaining):
    left = [loc[0]-1,loc[1]]
    right = [loc[0]+1,loc[1]]
    up = [loc[0],loc[1]+1]
    down = [loc[0],loc[1]-1]
    moves = [left,right,up,down]
    moves_valid = [is_valid_move(grid,loc,move,length_remaining) for move in moves]
    loop_check = 0
    while loop_check ==0:
        idx = random.randint(0,3)
        loop_check = moves_valid[idx]
    val_move = moves[idx]
    return val_move

def use_move(grid,move):
    grid[move[0]][move[1]] += 1
    return grid

def check_valid_path(grid,length):
    size = len(grid)
    valid = True
    valid &= all(grid[i][j]<=1 for i in range(size) for j in range(size))
    valid &= (sum(sum(grid,[])) == length+1)
    return valid

def trials_run(grid_size,path_length,num_trials):
    sim_results = []
    for i in range(num_trials):
        sim_results.append(gen_path(grid_size,path_length))
    weighted_paths = 0
    total_paths = 0
    for i in range(num_trials):
        weight = 1/sim_results[i][1]
        weighted_paths += sim_results[i][0]*weight
        total_paths += sim_results[i][0]
    return weighted_paths/total_paths

size = 11 
length = 13
trials = 10**5
print(trials_run(size,length,trials))
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 12:04:51 2017

@author: tran260
"""
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
#creates a board of size nxn
def build_board(dim):
    b = [[random.randint(0,1) for i in range(dim)] for j in range(dim)]
    return b


def populate(board,row,column,value):
    #populates a cell at a give row and column
    board[row][column] = value
    return board


def count_neighbors(board,row,column):
    neighbors = 0
    l = len(board)
    if board[row][column] == 1:
        neighbors -= 1
    for i in range(-1,2):
        for j in range(-1,2):
            neighbors += board[(row+i)%l][(column+j)%l]
    return neighbors

def create_neighbors_board(board):
    neighbors_count_board = [[0 for x in range(len(board))] for y in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board)):
            neighbors_count_board[i][j] = count_neighbors(board,i,j)
    return neighbors_count_board

def kill_or_revive_cells(neighbors_count_board,board):
    for i in range(len(board)):
        for j in range(len(board)):
            #insert logic here. for all that stuff
            #Exactly 2 means you can just go on
            if neighbors_count_board[i][j] == 2:
                next
            #less than 2 means it's dead no matter what
            elif neighbors_count_board[i][j] < 2:
                board[i][j] = 0
            #3 makes it alive no matter what
            elif neighbors_count_board[i][j] == 3:
                board[i][j] = 1
            else:
                board[i][j] = 0
    return board
def update(grid):
    global data
    neighbor_board = create_neighbors_board(grid)
    new_grid = kill_or_revive_cells(neighbor_board,grid)
    mat.set_data
    grid = new_grid
    return [mat]
grid = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,1]]
"""
fig,ax = plt.subplots()
mat = ax.mathshow(grid)
ani = animation.FuncAnimation(fig,update,interval = 50,save_count = 50)
plt.show
"""
def play_game(starting_board):
    #contin = "y"
    board = starting_board
    for i in range(100):
        neighbors_board = create_neighbors_board(board)
        board = kill_or_revive_cells(neighbors_board,board)
        plt.matshow(board)
        plt.show
    return 0


test_boart = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,1]]
#play_game(test_boart)

plt.matshow(test_boart)

plt.show

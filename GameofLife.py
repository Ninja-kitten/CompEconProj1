# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 12:04:51 2017

@author: tran260
"""
#creates a board of size nxn
def build_board(dim):
    b = [[0 for i in range(dim)] for j in range(dim)]
    return b

def populate(board,row,column,value):
    #populates a cell at a give row and column
    board[row][column] = value
    return board


def count_neighbors(board,row,column):
    neighbors = 0
    l = len(board)
    for i in range(-1,2):
        for j in range(-1,2):
            neighbors += board[(row+i)%l][(column+j)%l]
    return neighbors

def create_neighbors_board(board):
    neighbors_count_board = [[0 for x in range(len(board))] for y in range(len(board))]
    for i in len(board):
        for j in len(board):
            neighbors_count_board[i][j] = count_neighbors(board,i,j)
    return neighbors_count_board

def kill_or_revive_cells(neighbors_count_board,board):
    for i in range(len(board)):
        for j in range(len(board)):
            #insert logic here. for all that stuff
            if neighbors_count_board[i][j] < 2:
                board[i][j]= 0                     
    return board


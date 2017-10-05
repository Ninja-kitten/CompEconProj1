# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 22:18:27 2017

@author: tran2
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#dimensions
dim = 50
cells = [0,1]

#set up the board randomly
board = np.random.choice(cells,dim*dim,p = [.7,.3]).reshape(dim,dim)

#function that runs it.not 100% sure how funcAnim works.
#used  Author: electronut.in's conway.py file as a source
#their file doesn't update all at once so i modified it
def update(data):
    global board
    new_board = board.copy()
    neighbors = [[0 for i in range(dim)] for i in range(dim)]
    #creates a matrix of neighbors so it can update all cells at once
    for i in range(dim):
        for j in range(dim):
            for k in range(-1,2):
                for h in range(-1,2):
                    neighbors[i][j] += board[(i+h)%dim][(j+k)%dim]
            neighbors[i][j] -= board[i][j]
    #kills and revives cells
    for i in range(dim):
        for j in range(dim):
            if board[i][j] == 1:
                if neighbors[i][j] < 2 or neighbors[i][j] >3:
                    new_board[i][j] = 0
            else:
                if neighbors[i][j] == 3:
                    new_board[i][j] = 1
    #i really wish i knew what this one did...
    #i will probably use this as a reference for the rest of my programming life
    #because i still don't 100% know what's going on
    #and it scares me
    mat.set_data(new_board)
    board = new_board
    return [mat]

#setting up some parameters for the anim function
fig, ax = plt.subplots()
#this is for the function. We're setting up the subplot with the data from new_board
mat = ax.matshow(board)
#animation call. easy enough
anim = animation.FuncAnimation(fig,update,interval = 200,save_count = 50)
#and then we show it off
plt.show()
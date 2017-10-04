# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 13:29:23 2017

@author: tran260
"""

import random

#generate a list of n bidders, only returns the highest two
def toptwo_bidders(low,high, number_bidders):
    bidders = [random.randint(low,high) for i in range(number_bidders)]
    return sorted(bidders)[-2:]

def auction_result(bidders_list, start_price, reserve_price,increment):
    auction_winner = sorted(bidders_list)[-1]
    auction_loser = sorted(bidders_list)[-2]
    
    if auction_winner < reserve_price:
        return 0
    else:
        revenue = 0
        while revenue < auction_loser:
            if revenue + increment > auction_winner:
                break
            else:
                revenue += increment
        return revenue
    
def run_trials(trials, number_bidders, reserve_price, increment):
    
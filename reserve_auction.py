# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 13:29:23 2017

@author: tran260

rules
buyers 0-100 increments of 5
reserve 0-100 increments of 5
reserve price has the best revenue?
"""
import matplotlib.pyplot as plt
import random

#generate a list of n bidders, only returns the highest two
def toptwo_bidders(low,high, number_bidders):
    bidders = [random.randint(low,high)*5 for i in range(number_bidders)]
    return sorted(bidders)[-2:]

def auction_result(bidders_list, start_price, reserve_price,increment):
    auction_winner = sorted(bidders_list)[-1]
    auction_loser = sorted(bidders_list)[-2]
    
    if auction_winner < reserve_price:
        return 0
    else:
        revenue = 0
        while revenue < auction_loser or revenue < reserve_price:
            if revenue + increment > auction_winner:
                break
            else:
                revenue += increment
        return revenue
    
def run_trials(trials, number_bidders, reserve_price, increment):
    running_total = 0
    for i in range(trials):
        bidders = toptwo_bidders(0,20,number_bidders)
        running_total += auction_result(bidders,0,reserve_price,5)
    avg_rev = running_total/trials
    return avg_rev

reserve_prices = [i*5 for i in range(21)]
trials = 100000
bidders = 5
increment = 5
revenues = [run_trials(trials,bidders,reserv,increment) for reserv in reserve_prices]
print("Reserve Price \t Revenue")
for i in range(len(reserve_prices)):
    print(str(reserve_prices[i])+2*"\t"+str(revenues[i]))

plt.bar(reserve_prices,revenues, width = 3)
plt.ylabel("Revenue")
plt.xlabel("Reserve Prices")
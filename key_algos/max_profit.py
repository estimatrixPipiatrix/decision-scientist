# given a time series of stock closing prices, calculate in O(N)
# the greatest amount of money that could be made from a single
# buy followed by a single sell transaction

import numpy as np

def max_profit(prices):
    buy = np.inf
    sell = -np.inf
    profit = -np.inf
    max_profit = 0.0
    for p in prices:
        if p<buy:
            buy = p
            sell = -np.inf
        if p>sell:
            sell = p
        profit = sell-buy
        if profit>max_profit:
            max_profit = profit
    
    return max_profit

def max_profit_brute(prices):
    max_profit = 0.0
    for i,buy in enumerate(prices):
        for j,sell in enumerate(prices):
            if j>i and sell>buy:
                profit = sell-buy
                if profit>max_profit:
                    max_profit = profit
    return max_profit

for i in range(1000):
    length = np.random.randint(20)
    prices = np.random.randint(0,20,length)
    ans1 = max_profit(prices)
    ans2 = max_profit_brute(prices)
    if ans1!=ans2:
        print('answer mismatch')
        print(prices,ans1,ans2)

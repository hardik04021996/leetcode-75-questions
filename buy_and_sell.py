""" https://leetcode.com/problems/best-time-to-buy-and-sell-stock/ """

from typing import List

def max_profit(prices: List[int]) -> int:
    """ Return maximum profit from array ith element is price of a given stock on the ith day."""
    curr_min = prices[0]
    curr_max = 0
    profit = 0
    for price in prices:
        if price < curr_min:
            curr_min = price
            curr_max = 0
        elif price > curr_max:
            curr_max = price
            profit = max(profit, (curr_max-curr_min))
    return profit

print(max_profit([7,2,5,3,6,1,4,8]))

from typing import List
from leetcode.utils.driver import Driver

class Solution:
    """Key Point: Use two pointers. Left pointer tracks the lowest (buy) price. Right
    pointer always iterates.
    
    Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
    
    Method: Start buy_pointer at the first index and sell_pointer at the second index.
    At each loop, calculate the current value (sell value - buy value). Memorize new 
    max values. If buy pointer is > sell pointer, it should be moved. Sell pointer
    holds the current lowest value. Sell pointer should iterate at each loop (as if 
    days are moving foward).

    Returns:
        int: Maximum difference between a sell value and buy value in the list of prices.
    """
    @staticmethod
    def maxProfit(prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        buy_pointer = 0
        max_profit = 0
        
        for sell_pointer, current_price in enumerate(prices[1:], start=1):
            if (buy_price := prices[buy_pointer]) < current_price:
                current_profit = current_price - buy_price
                max_profit = max(max_profit, current_profit)
            else:
                buy_pointer = sell_pointer
            
        return max_profit

def main():
    input = {
        0: {
            "prices": [7,1,5,3,6,4]
        },
        1: {
            "prices": [7,6,4,3,1]
        }
    }
    output = [5, 0]
    Driver.run_test_cases(Solution.maxProfit, input, output)
    
if __name__ == '__main__':
    main()
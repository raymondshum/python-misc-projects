from typing import List
from leetcode.utils.driver import Driver

class Solution:
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
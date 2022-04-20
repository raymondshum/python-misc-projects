from leetcode.problems.utils.driver import Driver
from typing import List

class Solution:
    @staticmethod
    def search(nums: List[int], target: int) -> int:
        left_pointer = 0
        right_pointer = len(nums) - 1
        
        while left_pointer <= right_pointer:
            # This is actually a bug for very large or small numbers.
            # https://ai.googleblog.com/2006/06/extra-extra-read-all-about-it-nearly.html
            midpoint = (left_pointer + right_pointer) // 2
            
            if (current_value := nums[midpoint]) == target:
                return midpoint
            elif current_value > target:
                right_pointer = midpoint - 1
            else:
                left_pointer = midpoint + 1

        return -1
    
def main():
    input = {
        0: {
            "nums": [-1,0,3,5,9,12], 
            "target": 9
        },
        1: {
            "nums": [-1,0,3,5,9,12], 
            "target": 2
        },
        2: {
            "nums": [5],
            "target": 5
        },
        3: {
            "nums": [-1,0,3,5,9,12], 
            "target": 0
        },
    }

    output = [4, -1, 0, 1]
    Driver.run_test_cases(Solution.search, input, output)
    
if __name__ == '__main__':
    main()
from typing import List
from leetcode.utils.driver import Driver

class Solution:
    """Key Point: This is a binary search that estimates the index of
    a missing value rather than returning -1.

    Link: https://leetcode.com/problems/search-insert-position/
    
    Method: Binary search algorithm. However, if the value is not found: 
        1) Midpoint is the last one calculated when start_index = end_index.
        2) If the midpoint is < target, it means that the target should be in 
        the next sequential index (start_index in my implementation).
        3) Otherwise, it should be where the midpoint is (and the loop broke)
    
    Returns:
        int: Index number of value in the List or where it should be if it exists.
    """

    @staticmethod
    def searchInsert(nums: List[int], target: int) -> int:
        end_index = len(nums) - 1
        start_index = 0

        while start_index <= end_index:
            midpoint = int((end_index + start_index) / 2)
            if nums[midpoint] == target:
                return midpoint
            elif target > nums[midpoint]:
                start_index = midpoint + 1
            else:
                end_index = midpoint - 1

        if nums[midpoint] < target:
            return start_index
        else:
            return midpoint


if __name__ == '__main__':
    input = {
        0: {
            "nums": [1, 3, 5, 6],
            "target": 5
        },
        1: {
            "nums": [1, 3, 5, 6],
            "target": 2
        },
        2: {
            "nums": [1, 3, 5, 6],
            "target": 7
        },
        3: {
            "nums": [1, 3, 5, 6],
            "target": 0
        }

    }
    output = [2, 1, 4, 0]

    Driver.run_test_cases(Solution.searchInsert, input, output)

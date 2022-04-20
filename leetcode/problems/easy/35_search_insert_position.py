from typing import List
from leetcode.problems.utils.driver import Driver

class Solution:

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

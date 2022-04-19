from typing import List


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
    test_cases = {
        1: {
            "nums": [1, 3, 5, 6],
            "target": 5,
            "output": 2
        },
        2: {
            "nums": [1, 3, 5, 6],
            "target": 2,
            "output": 1
        },
        3: {
            "nums": [1, 3, 5, 6],
            "target": 7,
            "output": 4
        },
        4: {
            "nums": [1, 3, 5, 6],
            "target": 0,
            "output": 0
        }
    }

for case in test_cases:
    print(f"\nExecuting Test Case #{case}...")
    
    result = Solution.searchInsert(test_cases[case]["nums"], test_cases[case]["target"])
    
    if result != test_cases[case]["output"]:
        print(f"Test Failed. Expected Output = {test_cases[case]['output']} but Result = {result}")
    else:
        print("Test Passed!")
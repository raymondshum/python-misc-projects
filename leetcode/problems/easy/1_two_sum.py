from typing import List
from leetcode.problems.utils.driver import Driver

class Solution:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        """Key Point: Use dictionary (hash map) to store results.
        
        Link: https://leetcode.com/problems/two-sum/
        
        Method: Iterates through the list. If (target - current_value) is 
        not in the dictionary, we append its value and index. If it is in
        the dictionary, we can return the indicies of target and 
        current_value. This is because its presence in the dictionary lets
        us know that we have already encountered and logged the second
        number necessary to reach the target value.

        Returns:
            List: [index1, index2] where nums[index1] + nums[index2] == target
        """
        
        stored_results = {}
        
        for current_index, number in enumerate(nums):
            if (second_value:= target - number) in stored_results.keys():
                return [stored_results[second_value], current_index]
            else:
                stored_results[number] = current_index
    
def main():
    input = {
        0: {
            "nums": [2,7,11,15],
            "target": 9
        },
        1: {
            "nums": [3,2,4],
            "target": 6
        },
        2: {
            "nums": [3,3],
            "target": 6
        }
    }
    output = [[0,1], [1,2], [0,1]]
    Driver.run_test_cases(Solution.twoSum, input, output)

if __name__ == '__main__':
    main()
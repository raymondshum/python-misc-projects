from typing import List, Dict, Deque
from collections import deque
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        Key Point: Use hash map to track encountered numbers.

        Link: https://leetcode.com/problems/contains-duplicate-ii/

        Method: Probably not necessary to use Deque and popleft. Track
        encountered numbers in a dictionary with value being the index.
        When the same value is encountered again, calculate: 
        abs(curr_index - last_index). Return true if <= k.

        Returns: True if there is a duplicate matching the reqs
        and False if not.
        """
        value_map: Dict[int, Deque[int]] = {}
        for index, num in enumerate(nums):
            if num in value_map:
                if abs(value_map.get(num)[-1] - index) <= k:
                    return True
                else:
                    value_map[num].append(index) 
                    value_map[num].popleft()
            value_map[num] = deque([index])
        return False
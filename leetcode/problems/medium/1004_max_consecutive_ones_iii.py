class Solution:
    """
    Key Point: Sliding window. Window size is determined
    by "k" allowed flipped zeros.

    Link: https://leetcode.com/problems/max-consecutive-ones-iii/

    Method: Increase window until max number of flipped zeroes
    is exceeded. Retract window from the left until number of
    flipped zeroes equals max. Increase window size and repeat
    until no numbers remain.

    Returns: Max number of consecutive 1's in the list.
    """
    def longestOnes(self, nums: List[int], k: int) -> int:
        num_zeroes = 0
        max_length = 0
        left = 0
        for right, num in enumerate(nums):
            if num == 0:
                num_zeroes += + 1
            
            while num_zeroes > k:
                if nums[left] == 0:
                    num_zeroes -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)
        return max_length
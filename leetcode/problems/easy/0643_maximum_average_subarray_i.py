class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        Key Point: Sliding window problem with fixed
        width "k". Maintain moving average.

        Link: https://leetcode.com/problems/maximum-average-subarray-i/

        Method: See Key Point.

        Returns: float of maximum average
        """
        current_sum = sum(nums[:k])
        max_sum = current_sum
        left = 0
        right = k
        while right < len(nums):
            current_sum = current_sum - nums[left] + nums[right]
            left += 1
            right += 1
            max_sum = max(current_sum, max_sum)
        return max_sum / k
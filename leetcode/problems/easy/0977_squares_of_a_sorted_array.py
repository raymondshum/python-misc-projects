class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        Key Point: Two pointers. Maintain sorted order by
        comparing absolute values.

        Link: https://leetcode.com/problems/squares-of-a-sorted-array/

        Method: Left pointer at bottom and right pointer at
        top. Pointers move towards each other. Largest abs
        value is placed into the array from top down. This
        maintains sorted order if negatives are present.

        Returns: Sorted array of ints of increasing value.
        """
        right = len(nums) - 1
        left = 0
        result = [0] * len(nums)
        current_position = len(nums) - 1
        while left <= right:
            if abs(nums[left]) < abs(nums[right]):
                result[current_position] = nums[right] ** 2
                right -= 1
            else:
                result[current_position] = nums[left] ** 2
                left += 1
            current_position -= 1
            
        return result
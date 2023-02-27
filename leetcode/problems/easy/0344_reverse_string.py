class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Key Point: Can either use stack or two pointers. Two
        pointers uses less memory. 

        Link: https://leetcode.com/problems/reverse-string/

        Method: Swap letters at both ends until pointers meet.

        Returns: Nothing. In place swap.
        """
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return
"""
Given an integer x, return true if x is a
palindrome, and false otherwise.

Example :

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Convert to string
        x = str(x)
        # Check if the string is equal to the reverse of the string
        return x == x[::-1]
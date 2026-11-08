"""
Problem: Two Sum
LeetCode: #1
Difficulty: Easy
Topic: Array, Hash Table

Approach:
Hash Map

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numbers = {}

        for index, num in enumerate(nums):
            if target - num in numbers:
                return [numbers[target - num], index]

            numbers[num] = index

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums_set = set(nums)
        length = 0

        for num in nums:
            if num - 1 in nums_set:
                continue

            current_num  = num
            current_length = 1

            while current_num + 1 in nums_set:
                current_num += 1
                current_length += 1

            length = max(length, current_length)
        
    return length

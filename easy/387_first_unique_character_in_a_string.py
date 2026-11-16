class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_Count = {}

        for char in s:
            char_Count[char] = char_Count.get(char, 0) + 1

        for index, char in enumerate(s):
            if char_Count[char] == 1:
                return index

        return -1

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        strs_sorted = {}

        for word in strs:
            key = "".join(sorted(word))

            if key not in strs_sorted:
                strs_sorted[key] = []

            strs_sorted[key].append(word)

        return [*strs_sorted.values()]
        

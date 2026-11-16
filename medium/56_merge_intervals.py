class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        new_intervals = [intervals[0]]

        for interval in intervals[1:]:
            last = new_intervals[-1]

            if interval[0] <= last[1]:
                new_intervals[-1] = [last[0], max(last[1], interval[1])]
            else:
                new_intervals.append(interval)

        return new_intervals
        

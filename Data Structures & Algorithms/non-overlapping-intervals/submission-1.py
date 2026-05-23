class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 0


        intervals.sort(key=lambda x: (x[0],x[1]))

        res = 0
        for i,inter in enumerate(intervals):
            if i == 0:
                right = inter[1]
            elif inter[0] < right:
                res += 1
                right = min(inter[1],right)
            else:
                right = inter[1]

        return res

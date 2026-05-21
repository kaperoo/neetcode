class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]

        opt = []
        inserted = False
        left,right = None,None
        for i,inter in enumerate(intervals):
            if inter[0]<=newInterval[0]<=inter[1]:
                left = inter[0]
                right = max(newInterval[1],inter[1])
                inserted = True
            elif newInterval[0] < inter[0] and not inserted:
                inserted = True
                left = newInterval[0]
                if newInterval[1] < inter[0]:
                    opt.append(newInterval)
                    opt.append(inter)
                else:
                    right = max(newInterval[1],inter[1])
            elif right and right >= inter[0]:
                right = max(right,inter[1])
            elif right and right < inter[0]:
                opt.append([left,right])
                opt.append(inter)
                right = None
            else:
                opt.append(inter)
        
        if right:
            opt.append([left,right])
        if not inserted:
            opt.append(newInterval)

        return opt

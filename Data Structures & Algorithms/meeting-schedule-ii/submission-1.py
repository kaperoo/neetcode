"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = []
        end = []

        for i in intervals:
            start.append(i.start)
            end.append(i.end)
        
        start.sort()
        end.sort()

        print(start)
        print(end)

        i,j = 0,0

        max_rooms = 0
        rooms = 0

        while i < len(start):
            if start[i] < end[j]:
                rooms += 1
                max_rooms = max(max_rooms,rooms)
                i += 1
            else:
                j += 1
                rooms -= 1

        return max_rooms

        
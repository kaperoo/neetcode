import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            s1 = heapq.heappop_max(stones)
            s2 = heapq.heappop_max(stones)

            res = s1-s2

            if res: heapq.heappush_max(stones,res)

        if len(stones):
            return heapq.heappop_max(stones)
        return 0

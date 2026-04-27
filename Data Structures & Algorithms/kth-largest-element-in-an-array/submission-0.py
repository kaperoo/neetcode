class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapq.heapify(heap)
        for n in nums:
            heapq.heappush(heap,-n)

        ret = None
        for i in range(k):   
            ret = -heapq.heappop(heap)

        return ret
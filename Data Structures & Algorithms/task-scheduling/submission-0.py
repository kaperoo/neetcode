class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        seen = {}
        heap = []
        heapq.heapify(heap)

        for t in tasks:
            curr = seen.get(t,0)

            heapq.heappush(heap,(curr,t))

            seen[t] = curr + n+1

        i = 0
        while len(heap) > 0:
            if heap[0][0]<=i:
                heapq.heappop(heap)
            i+=1
        
        return i
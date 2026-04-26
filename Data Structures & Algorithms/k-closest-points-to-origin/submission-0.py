class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)
        for p in points:
            heapq.heappush(heap, (self.dist(p[0],p[1]), p))
        
        opt = []
        for i in range(k):
            _,point = heapq.heappop(heap)
            opt.append(point)
        return opt

    def dist(self,x,y):
        return math.sqrt(x**2+y**2)  
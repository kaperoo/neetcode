class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        l = len(points)
        dist = []

        e = UFind(l)

        for i in range(l):
            for j in range(i):
                dist.append((self.man(points[i],points[j]), i, j))
        
        dist.sort()

        min_dist = 0

        for d in dist:
            if e.find(d[1]) != e.find(d[2]):
                min_dist += d[0]
                e.unite(d[1],d[2]) 


        return min_dist

    def man(self, a, b):
        return abs(a[0]-b[0]) + abs(a[1]-b[1]) 

class UFind:
    def __init__(self,size):
        self.parent = list(range(size))
    def find(self,i):
        if self.parent[i] == i:
            return i
        else: return self.find(self.parent[i])
    def unite(self, i, j):
        irep = self.find(i)
        jrep = self.find(j)

        self.parent[irep] = jrep


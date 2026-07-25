class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        fs = {}
        costs = [float('inf') for _ in range(n)]
        costs[src] = 0
        stops = [0 for _ in range(n)]

        heap = []

        for f in flights:
            if not fs.get(f[0]):
                fs[f[0]] = []
            fs[f[0]].append((f[2],f[1]))

        seen = set()

        curr = src
        while True:
            seen.add(curr)

            for f in fs.get(curr,[]):
                if f[1] not in seen and stops[curr] <= k:
                    heapq.heappush(heap,(f[0]+costs[curr],f[1],stops[curr]+1))
            if len(heap) == 0:
                break
            new_cost, curr, ns = heapq.heappop(heap)
            stops[curr] = ns
            costs[curr] = new_cost
            if curr == dst:
                break

        return costs[dst] if costs[dst] != float('inf') else -1

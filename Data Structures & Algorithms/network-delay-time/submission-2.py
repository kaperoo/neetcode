import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        best = {i:float('inf') for i in range(1,n+1)}

        best[k] = 0
        con = {}
        seen = set([k])

        for c in times:
            con[c[0]] = con.get(c[0],[])
            con[c[0]].append([c[1],c[2]])

        queue = [(0,k)]
        heapq.heapify(queue)
        while True:
            if not queue:
                break
            node = heapq.heappop(queue)[1]
            for c in con.get(node,[]):
                time = best[node]+c[1]
                best[c[0]] = min(best[c[0]], time)
                if c[0] not in seen:
                    seen.add(c[0])
                    heapq.heappush(queue,(time,c[0]))

        opt = max(best.values())
        return opt if opt != float('inf') else -1
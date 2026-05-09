class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.nodes = {i:set() for i in range(n)}
        for e in edges:
            self.nodes[e[0]].add(e[1])
            self.nodes[e[1]].add(e[0])

        self.seen = set()
        conn = 0
        for i in range(n):
            if i in self.seen:
                continue
            self.search(i)
            conn +=1
        return conn

    def search(self,i):
        if i in self.seen:
            return
        self.seen.add(i)
        for c in self.nodes[i]:
            self.search(c)
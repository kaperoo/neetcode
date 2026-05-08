class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        self.nodes = {i: set() for i in range(n)}
        for e in edges:
            self.nodes[e[0]].add(e[1])
            self.nodes[e[1]].add(e[0])

        for i in range(n):
            num = self.recurse(i,set(),-1)
            print(num)
            if num == -1:
                return False
            elif num == n:
                return True
        return False


    def recurse(self,i,s,prev):
        if i in s:
            return -1
        s.add(i)

        nds = 0
        for n in self.nodes[i]:
            if n == prev:
                continue
            num = self.recurse(n,s,i)
            if num == -1:
                return -1
            nds += num
        return nds+1
        
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # seen = set()
        # ret = []
        # for x,y in edges:
        #     if x in seen and y in seen:
        #         ret.append([x,y])
        #     seen.add(x)
        #     seen.add(y)
        
        # return ret[-1]
        self.nodes = {}

        for x,y in edges:
            self.nodes[x] = self.nodes.get(x,x)
            self.nodes[y] = self.nodes.get(y,y)

            a = self.reduce(self.nodes[x])
            b = self.reduce(self.nodes[y])

            if a == b:
                return [x,y]
            
            self.nodes[b] = a



    def reduce(self,i):
        while self.nodes[i] != i:
            i = self.nodes[i]
        return i
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.nodes = {i:set() for i in range(numCourses)}
        # self.poss = {i for i in range(numCourses)}
        for edge in prerequisites:
            self.nodes[edge[0]].add(edge[1])
        
        self.res = []
        for n in range(numCourses):
            # if len(self.nodes[n]) == 0:
            #     self.res.append(n)
            if not self.recurse(n,set()):
                return []
        
        return self.res

    
    def recurse(self,i,s):
        seen = s.copy()
        if i in seen:
            return False
        seen.add(i)
        if i not in self.nodes:
            return True
        elif len(self.nodes[i]) != 0:
            # self.res.append(i)
            # del self.nodes[i]
            # return True

            for c in self.nodes[i]:
                if not self.recurse(c,seen):
                    return False
        
        self.res.append(i)
        del self.nodes[i]
        return True
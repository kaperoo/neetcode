class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.nodes = {}
        for i in range(numCourses):
            self.nodes[i] = set()

        for edge in prerequisites:
            # self.nodes[edge[0]] = self.nodes.get(edge[0],set())
            self.nodes[edge[0]].add(edge[1])
            # self.nodes[edge[1]] = self.nodes.get(edge[1],set())

        self.truths = [False]*numCourses
        print(self.nodes)
        for i in range(numCourses):
            if not self.search(i,set()):
                return False

        return True

    def search(self,i,s):
        seen = s.copy()
        if len(self.nodes[i]) == 0 or self.truths[i]:
            self.truths[i] = True
            return True
        if i in seen:
            return False
        
        seen.add(i)
        for j in self.nodes[i]:
            # self.truths[i] = self.search(j,seen)
            if not self.search(j,seen):
                return False
        return True

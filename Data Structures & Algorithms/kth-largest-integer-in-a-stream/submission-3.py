import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.q = []

        for i in range(len(nums)):
            if i ==0:
                self.q.append(nums[i])
                continue
            for j in range(len(self.q)):
                if nums[i] > self.q[j]:
                    self.q.insert(j, nums[i])
                    if len(self.q) > k:
                        self.q.pop()
                    break
            else:
                if len(self.q) < k:
                    self.q.append(nums[i])
        


    def add(self, val: int) -> int:
        if len(self.q) == 0:
            self.q.append(val)
            return val

        for i in range(len(self.q)):
            if self.q[i] < val:
                self.q.insert(i,val)
                if len(self.q) > self.k:
                    self.q.pop()
                break
        else:
            if len(self.q) < self.k:
                self.q.append(val)

        return self.q[self.k-1]


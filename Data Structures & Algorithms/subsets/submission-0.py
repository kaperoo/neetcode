class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.recurse(0, nums)
    
    def recurse(self, start, nums):
        if len(nums) == start:
            return [[]]

        res = self.recurse(start+1,nums)  
        for r in range(len(res)):
            res.append([nums[start]] + res[r])

        return res
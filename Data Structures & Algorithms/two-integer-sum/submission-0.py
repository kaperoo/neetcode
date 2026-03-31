class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,n in enumerate(nums):
            rest = target - n
            if rest in seen:
                return [seen[rest], i]
            
            seen[n] = i
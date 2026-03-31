class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h = {}
        for i in nums:
            if h.get(i, 0):
                return True
            else:
                h[i] = 1

        return False
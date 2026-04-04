class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        d = 0
        m = -1
        for i in nums:
            d += i

        c = len(nums)/2 * (len(nums)+1)

        return int(c-d)
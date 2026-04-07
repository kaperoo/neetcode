class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        max_sum = float('-inf')
        s = 0

        for n in nums:
            if s < 0:
                s = 0
            s += n
            if s > max_sum:
                max_sum = s

        return max_sum
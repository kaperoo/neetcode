class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last = len(nums)-1
        i = 0
        prev_i = None
        while True:
            if i==prev_i:
                return False
            elif i >= last:
                return True

            max_jump = 0
            idx = 0
            for x in range(1,nums[i]+1):
                if x+i >= last:
                    return True
                if i+x+nums[x+i] > max_jump:
                    max_jump = i+x+nums[x+i]
                    idx = x

            prev_i = i
            i += idx
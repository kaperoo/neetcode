class Solution:
    def jump(self, nums: List[int]) -> int:
        
        jumps = 0
        i = 0

        while i < len(nums)-1:
            max_jump = 0
            jp = 0
            for j in range(1,nums[i]+1):
                if i+j > len(nums)-1:
                    return jumps + 1
                jump = nums[i+j] + i + j
                if jump >= max_jump or jump >= len(nums)-1:
                    max_jump = jump
                    jp = j

            i += jp
            jumps += 1

        return jumps

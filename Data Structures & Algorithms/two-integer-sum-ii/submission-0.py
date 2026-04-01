class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for l in range(len(numbers)):
            for r in range(len(numbers)-1,l,-1):
                if numbers[r] == target-numbers[l]:
                    return[l+1,r+1]

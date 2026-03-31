class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        for n in nums:
            seen.add(n)

        print(seen)

        max_count = 0
        for n in seen:
            x = n
            count = 0
            while x in seen:
                count += 1
                x += 1
            if count > max_count:
                max_count = count

        return max_count
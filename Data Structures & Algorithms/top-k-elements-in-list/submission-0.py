class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0) + 1
        
        fs = list(freq)
        fs.sort(key=lambda x: freq[x])
        return fs[-k:]
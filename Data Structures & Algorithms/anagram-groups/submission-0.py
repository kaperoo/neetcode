class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []
        hashes = []
        for word in strs:
            h = {}
            for c in word:
                h[c] = h.get(c,0)+1

            for i in range(len(hashes)):
                if h == hashes[i]:
                    groups[i].append(word)
                    break
            else:
                hashes.append(h)
                groups.append([word])            

        return groups
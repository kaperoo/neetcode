class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        if len(triplets) == 1:
            if triplets[0] == target:
                return True
            return False

        ts = [[],[],[]]

        for i in range(3):
            for t in triplets:

                if t[i] != target[i]:
                    continue

                truths = True
                for j in range(3):
                    if j == i:
                        continue
                    elif t[j] > target[j]:
                        truths = False
                        break

                if truths:
                    ts[i] = t
                # if t[i] == target[i] and :
                #     ts[i] = t

        if all(ts):
            return True
        return False
        
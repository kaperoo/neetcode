class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        sd = {}

        for i,c in enumerate(s):
            sd[c] = sd.get(c,[i,i])
            sd[c][1] = i
        
        ints = []
        for i in sd.items():
            if ints:
                if ints[-1][1]>i[1][0]:
                    ints[-1][1] = max(ints[-1][1],i[1][1])
                else:
                    ints.append(i[1])
            else:
                ints.append(i[1])

        opt = []
        for i in ints:
            opt.append(i[1]-i[0]+1)
        return opt
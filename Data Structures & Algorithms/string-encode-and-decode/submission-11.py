class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return '{empty}'

        opt = strs[0]
        for i in range(1, len(strs)):
            opt += '{div}' + strs[i]
        
        return opt

    def decode(self, s: str) -> List[str]:
        if s is '{empty}':
            return []
        strs = s.split('{div}')
        return strs
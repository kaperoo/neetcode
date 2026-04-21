class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        opt = set(tuple())
        nums.sort()

        for n in nums:
            new_set = set()
            for o in opt:
                new_set.add((*o,n))
            opt = opt|new_set
            opt.add((n,))

        opt = list(map(lambda x: list(x), opt))
        opt.append([])
        return opt

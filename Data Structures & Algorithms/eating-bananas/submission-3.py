class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = max(sum(piles)//h,1)
        mid = (r+l)//2
        last_min = -1
        while l <= r:
            t = self.eat(mid,piles)
            # if t == h:
            #     return mid
            if t > h:
                l = mid + 1
            else:
                last_min = mid
                r = mid - 1
            mid = (r+l)//2

        return last_min
        # return mid

    def eat(self, rate, piles):
        time = 0
        for p in piles:
            # while p > 0:
            #     p -= rate
            #     time += 1
            time += math.ceil(p/rate)
            # print(p, time)
        return time
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen: return False
            seen.add(n)

            c = 0
            while n != 0:
                c += (n%10)**2
                n = (n-(n%10))/10
            n = c
        return True
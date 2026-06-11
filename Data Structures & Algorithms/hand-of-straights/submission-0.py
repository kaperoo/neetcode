class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()

        if len(hand)%groupSize != 0:
            return False

        groups = {i:[] for i in range(int(len(hand)/groupSize))}

        for i in range(len(hand)):
            for g in groups:
                if len(groups[g]) == 0 or groups[g][-1] == hand[i]-1:
                    groups[g].append(hand[i])

                    if len(groups[g]) == groupSize:
                        del groups[g]
                    break

        print(groups)

        if len(groups) == 0:
            return True
        return False
 
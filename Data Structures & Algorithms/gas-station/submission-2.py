class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        min_tank = 0
        min_idx = -1
        tank = 0
        for i in range(len(cost)):
            tank += gas[i] - cost[i]

            if tank < min_tank:
                min_idx = i
                min_tank = tank
            # if tank < 0:
            #     neg_idx = i

        # if neg_idx is None:
        #     return 0
        if tank >=0:
            # return neg_idx +1 if (neg_idx+1) < len(gas) else 0
            return min_idx + 1 if min_idx+1<len(gas) else 0
        else:
            return -1
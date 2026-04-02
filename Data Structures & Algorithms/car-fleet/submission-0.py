class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        cars = list(zip(position, speed))
        cars.sort(key=lambda x: x[0])

        for i in range(len(cars)):

            fin = (target - cars[i][0])/cars[i][1]
            
            while stack and fin >= stack[-1]:
                stack.pop()

            stack.append(fin)



        return(len(stack)) 
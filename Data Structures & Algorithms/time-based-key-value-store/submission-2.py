class TimeMap:

    def __init__(self):
        self.m = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key] = self.m.get(key, dict())
        self.m[key][timestamp] = value


    def get(self, key: str, timestamp: int) -> str:

        if not self.m.get(key,None):
            return ""

        stamps = list(self.m[key].keys())

        left = 0
        right = len(stamps)-1
        mid = (left + right)//2
        closest = -1


        while left <= right:
            if stamps[mid] == timestamp:
                return self.m[key][stamps[mid]]
            elif stamps[mid] < timestamp:
                closest = stamps[mid]
                left = mid + 1
            else:
                right = mid - 1
            
            mid = (left+right)//2

        if closest >= 0:
            return self.m[key][closest]
        return ""
        



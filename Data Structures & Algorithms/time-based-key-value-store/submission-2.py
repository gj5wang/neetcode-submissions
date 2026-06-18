class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        #if keys dont exist create list
        if key not in self.store:
            self.store[key] = []

        self.store[key].append((timestamp, value))
    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.store:
            return ""
        
        values = self.store[key]
        left = 0
        right = len(values) - 1
        res = ""

        while left <= right:
            mid = (left + right) // 2
            t,v = values[mid]


            if (t <= timestamp):
                res = v        # valid candidate
                left = mid + 1  # try to find later one
            else:
                right = mid - 1

        return res

        
#basically u need to find the largest timestamp  smaller than the given value
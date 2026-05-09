class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        arr = self.time_map[key]
        l, r = 0, len(arr)
        while l < r:
            m = (l + r) // 2
            if arr[m][0] >= timestamp + 1:
                r = m
            else:
                l = m + 1
        # print(key, timestamp, l)
        # if l == len(arr):
        #     return ""
        if l == 0:
            return ""
        return arr[l - 1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
